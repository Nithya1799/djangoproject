from django.db import models

from django.contrib.auth.models import AbstractUser

# customUserModel  definition
class CustomUser(AbstractUser):
    phone=models.IntegerField()
    address=models.TextField()
