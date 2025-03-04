from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField(null=True)

    def __str__(self) -> str:
        return self.username
    

class Account(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='accounts')
    name = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=12, decimal_places=2)
    account_type = models.CharField(max_length=50, choices=[
        ('savings', 'Savings'),
        ('checking', 'Checking'),
        ('credit', 'Credit'),
        ('salary', 'Salary')
    ])  # e.g., "Savings", "Checking", "Credit"
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name