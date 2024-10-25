from django.contrib import admin

from transactions import models

# Register your models here.
admin.site.register(models.Category)
admin.site.register(models.Transaction)