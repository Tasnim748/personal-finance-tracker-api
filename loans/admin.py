from django.contrib import admin

from loans import models

# Register your models here.
admin.site.register(models.Loan)
admin.site.register(models.LoanPayment)