from django.db import models

from accounts.models import Account

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(
        max_length=50,
        choices=[
            ('expense', 'Expense'),
            ('income', 'Income'),
        ]
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.type})"

    class Meta:
        verbose_name_plural = "Categories"


class Transaction(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='transactions')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='transactions')
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    description = models.TextField(blank=True)
    date = models.DateField()
    is_recurring = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.category.type} - {self.amount} - {self.date}"
    
    @property
    def transaction_type(self):
        """
        Returns the transaction type based on the category
        """
        return self.category.type if self.category else None