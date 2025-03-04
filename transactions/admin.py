from django.contrib import admin

from transactions import models

# Register your models here.
admin.site.register(models.Category)


@admin.register(models.Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('account', 'date', 'amount', 'category', 'is_recurring')
    list_filter = ('date', 'category__name')