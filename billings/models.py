from django.db import models
from accounts.models import Account

# Create your models here.
class UtilityBill(models.Model):
    BILL_TYPES = [
        ('electricity', 'Electricity'),
        ('water', 'Water'),
        ('gas', 'Gas'),
        ('internet', 'Internet'),
        ('phone', 'Phone'),
        ('other', 'Other'),
    ]

    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='bills')
    bill_type = models.CharField(max_length=20, choices=BILL_TYPES)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    due_date = models.DateField()
    is_paid = models.BooleanField(default=False)
    paid_date = models.DateField(null=True, blank=True)
    billing_period_start = models.DateField()
    billing_period_end = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.bill_type} - {self.due_date}"