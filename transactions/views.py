import datetime
from rest_framework import generics
from .serializers import ExpenseGetSerializer, ExpenseCreateSerializer
from .models import Expense
from django.db.models import F

from rest_framework.authentication import SessionAuthentication
from rest_framework import permissions, status
from rest_framework.response import Response

from accountManagement.customAuthToken import TokenAuthentication
from accountManagement.models import User

from .permissions import ExpenseDetailAuthorizationPermission

# Create your views here.
class ExpenseDetailAPIView(generics.RetrieveAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseGetSerializer
    authentication_classes = [
        TokenAuthentication,
        SessionAuthentication
    ]
    permission_classes = [
        ExpenseDetailAuthorizationPermission
    ]


class ExpensesAPIView(generics.ListCreateAPIView):
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ExpenseGetSerializer
        return ExpenseCreateSerializer

    authentication_classes = [
        TokenAuthentication,
        SessionAuthentication
    ]
    permission_classes = [
        permissions.IsAuthenticated
    ]


    def get_queryset(self):
        user = self.request.user
        currentYear = datetime.date.today().year
        expenses = user.expenses.all()

        if self.request.query_params.get('category'):
            category = self.request.query_params.get('category').title()
            expenses = expenses.filter(typeRef__name=category)

        if self.request.query_params.get('min_month'):
            minMonth = self.request.query_params.get('min_month')
            expenses = expenses.filter(dueDate__month__gte=minMonth, dueDate__year=currentYear)
       
        if self.request.query_params.get('max_month'):
            maxMonth = self.request.query_params.get('max_month')
            expenses = expenses.filter(dueDate__month__lte=maxMonth, dueDate__year=currentYear)

        if self.request.query_params.get('due'):
            due = self.request.query_params.get('due')
            expenses = expenses.filter(amount__gte=F('paid') + due)

        return expenses
    
    def perform_create(self, serializer):
        serializer.save(personRef=self.request.user)

