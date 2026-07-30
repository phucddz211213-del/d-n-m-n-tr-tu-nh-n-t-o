from rest_framework import serializers
from .models import Category, Transaction, Budget, Goal, AIRequest

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        read_only_fields = ('user','created_at')

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'
        read_only_fields = ('user','created_at')

class BudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Budget
        fields = '__all__'
        read_only_fields = ('user','created_at')

class GoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goal
        fields = '__all__'
        read_only_fields = ('user','created_at')

class AIRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = AIRequest
        fields = '__all__'
        read_only_fields = ('user','redacted','created_at','response')
