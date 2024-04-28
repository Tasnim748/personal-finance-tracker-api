from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField(null=True)

    def __str__(self) -> str:
        return self.first_name + " " + self.last_name
    