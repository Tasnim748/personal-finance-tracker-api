from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.ExpenseType)
admin.site.register(models.Expense)