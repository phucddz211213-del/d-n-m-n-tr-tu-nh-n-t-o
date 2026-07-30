from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from expenses.models import Transaction, AIRequest
from django.db.models import Sum
from .client import AIClient

class AIReportView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        profile = getattr(request.user, "profile", None)
        if not profile or not profile.ai_opt_in:
            return Response({"detail":"User has not opted into AI features."}, status=status.HTTP_403_FORBIDDEN)
        month = request.data.get("month")
        if not month:
            return Response({"detail":"month required (YYYY-MM)."}, status=status.HTTP_400_BAD_REQUEST)
        qs = Transaction.objects.filter(user=request.user, date__startswith=month)
        cats = qs.values('category__name').annotate(total=Sum('amount')).order_by('-total')
        categories = [{"name": c.get("category__name") or "Không rõ", "total": float(c.get("total") or 0)} for c in cats]
        summary = {"month": month, "categories": categories}
        ai = AIClient()
        prompt = ai.build_monthly_report_prompt(summary)
        redacted = ai.redact_for_logging(summary)
        response_text = ai.call(prompt)
        AIRequest.objects.create(user=request.user, request_type='monthly_report', input_summary=redacted, response=response_text)
        return Response({"report": response_text})
