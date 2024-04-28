from django.db import models
from accountManagement.models import User

# Create your models here.
class ExpenseType(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self) -> str:
        return self.name
    

class Expense(models.Model):
    name = models.CharField(max_length=50)
    dueDate = models.DateField()
    amount = models.DecimalField(decimal_places=2, max_digits=15, null=True)
    typeRef = models.ForeignKey(ExpenseType, on_delete=models.SET_NULL, related_name='expenses', null=True)
    personRef = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='expenses')
    paid = models.DecimalField(decimal_places=2, max_digits=15, null=True)

    def __str__(self) -> str:
        return self.name

    @property
    def due(self):
        if self.amount and self.paid:
            return self.amount - self.paid
        return
    
    @property
    def type(self):
        return self.typeRef.name
    
    @property
    def person(self):
        return str(self.personRef)
    

class SuddenExpense(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateField(auto_now_add=True)
    amount = models.DecimalField(decimal_places=2, max_digits=10, null=True)
    personRef = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='suddenExpenses')

    @property
    def person(self):
        return str(self.personRef)


class Loan(models.Model):
    amount = models.DecimalField(decimal_places=2, max_digits=15)
    dueDate = models.DateField()
    paid = models.DecimalField(decimal_places=2, max_digits=15)
    personRef = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='loans')
    description = models.CharField(max_length=50, unique=True)

    @property
    def due(self):
        return self.amount - self.paid

    @property
    def person(self):
        return str(self.personRef)