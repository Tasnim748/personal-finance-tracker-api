from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts import models

# Register your models here.
class CustomUserAdmin(UserAdmin):
    fieldsets = [
        *UserAdmin.fieldsets,
        ("Additional Info", {"fields": ["date_of_birth"]}),
    ]


admin.site.register(models.User, CustomUserAdmin)
admin.site.register(models.Account)