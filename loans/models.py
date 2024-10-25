from django.db import models

from accounts.models import Account

# Create your models here.
class Loan(models.Model):
    LOAN_TYPES = [
        ('personal', 'Personal'),
        ('home', 'Home'),
        ('car', 'Car'),
        ('education', 'Education'),
        ('other', 'Other'),
    ]

    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    loan_type = models.CharField(max_length=20, choices=LOAN_TYPES)
    principal_amount = models.DecimalField(max_digits=12, decimal_places=2)
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2)  # Annual interest rate
    start_date = models.DateField()
    end_date = models.DateField()
    monthly_payment = models.DecimalField(max_digits=12, decimal_places=2)
    remaining_balance = models.DecimalField(max_digits=12, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.loan_type} - {self.principal_amount}"
    

class LoanPayment(models.Model):
    loan = models.ForeignKey(Loan, on_delete=models.CASCADE)
    payment_date = models.DateField()
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    principal_payment = models.DecimalField(max_digits=12, decimal_places=2)
    interest_payment = models.DecimalField(max_digits=12, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment for {self.loan} - {self.payment_date}"