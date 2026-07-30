from django.db import models
from django.conf import settings

class Category(models.Model):
    TYPE_CHOICES = (('income','Income'), ('expense','Expense'))
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='categories')
    name = models.CharField(max_length=120)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.name} ({self.type})"

class Transaction(models.Model):
    TYPE_CHOICES = (('income','Income'), ('expense','Expense'))
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='transactions')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='transactions')
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    currency = models.CharField(max_length=10, default='VND')
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    note = models.TextField(blank=True, null=True)
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

class Budget(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='budgets')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    month = models.CharField(max_length=7)  # YYYY-MM
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    threshold_percent = models.PositiveSmallIntegerField(default=90)
    created_at = models.DateTimeField(auto_now_add=True)

class Goal(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='goals')
    name = models.CharField(max_length=200)
    target_amount = models.DecimalField(max_digits=12, decimal_places=2)
    current_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    target_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class AIRequest(models.Model):
    REQUEST_TYPES = (('monthly_report','Monthly Report'), ('budget_suggest','Budget Suggestion'), ('qa','QA'))
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='ai_requests')
    request_type = models.CharField(max_length=30, choices=REQUEST_TYPES)
    input_summary = models.JSONField()
    redacted = models.BooleanField(default=True)
    response = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
