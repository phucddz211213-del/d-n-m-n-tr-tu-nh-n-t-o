from django.core.management.base import BaseCommand
from django.db.models import Sum
from expenses.models import Budget, Transaction
from django.core.mail import send_mail
from django.conf import settings

class Command(BaseCommand):
    help = "Check budgets for the current month and send email alerts"

    def add_arguments(self, parser):
        parser.add_argument("--month", type=str, help="Month in YYYY-MM (default: current month)")

    def handle(self, *args, **options):
        import datetime
        month = options.get("month")
        if not month:
            now = datetime.date.today()
            month = f"{now.year}-{now.month:02d}"
        budgets = Budget.objects.filter(month=month)
        for b in budgets:
            total = Transaction.objects.filter(user=b.user, category=b.category, date__startswith=month).aggregate(sum=Sum('amount'))['sum'] or 0
            total = float(total)
            warn_at = float(b.amount) * (b.threshold_percent / 100.0)
            if total >= warn_at:
                subject = f"Cảnh báo: Ngân sách {b.category.name if b.category else 'Tổng'} tháng {month}"
                message = f"Bạn đã chi {total} trong tháng {month} cho {b.category.name if b.category else 'danh mục'}, ngân sách {b.amount}. Vượt ngưỡng {b.threshold_percent}%."
                recipient = [b.user.email] if b.user.email else []
                if recipient:
                    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, recipient)
                    self.stdout.write(self.style.SUCCESS(f"Alert sent to {b.user.email} for budget {b.id}"))
                else:
                    self.stdout.write(self.style.WARNING(f"User {b.user.username} has no email, cannot send alert."))
