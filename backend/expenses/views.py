from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.db.models import Sum
from .models import Category, Transaction, Budget, Goal
from .serializers import CategorySerializer, TransactionSerializer, BudgetSerializer, GoalSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return Category.objects.filter(user=self.request.user)
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class TransactionViewSet(viewsets.ModelViewSet):
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        qs = Transaction.objects.filter(user=self.request.user)
        start = self.request.query_params.get('start')
        end = self.request.query_params.get('end')
        cat = self.request.query_params.get('category')
        q = self.request.query_params.get('q')
        if start:
            qs = qs.filter(date__gte=start)
        if end:
            qs = qs.filter(date__lte=end)
        if cat:
            qs = qs.filter(category_id=cat)
        if q:
            qs = qs.filter(note__icontains=q)
        return qs.order_by('-date')
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class BudgetViewSet(viewsets.ModelViewSet):
    serializer_class = BudgetSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return Budget.objects.filter(user=self.request.user)
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class GoalViewSet(viewsets.ModelViewSet):
    serializer_class = GoalSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return Goal.objects.filter(user=self.request.user)
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
