from django.db import models
from django.contrib.auth.models import AbstractUser
from random import randint
class CustomUser(AbstractUser):
    phone=models.IntegerField(default=0)
    address=models.TextField(default=" ")
    role=models.CharField(max_length=20,default=" ")
    is_verified=models.BooleanField(default=False)
    otp=models.CharField(max_length=10,null=True,blank=True)

    def generate_otp(self):
        otp_number=str(randint(1000,9999))+str(self.id)
        self.otp=otp_number
        self.save()