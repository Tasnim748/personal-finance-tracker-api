from rest_framework import serializers
from .models import Expense

class ExpenseGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = ['id', 'name', 'dueDate', 'amount', 'type', 'person', 'paid', 'due', 'typeRef']

class ExpenseCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = ['id', 'name', 'dueDate', 'amount', 'type', 'person', 'paid', 'due', 'typeRef', 'personRef']