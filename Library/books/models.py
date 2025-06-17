from django.db import models
from random import randint
from django.contrib.auth.models import AbstractUser

# customUserModel  definition
class CustomUser(AbstractUser):
    phone=models.IntegerField()
    address=models.TextField()
    is_verified=models.BooleanField(default=False) #after verification it will set to true
    otp=models.CharField(max_length=10,null=True,blank=True) #to store the generated otp in backend table


    def generate_otp(self):
        # for creating  otp number for verification

        otp_number=str(randint(1000,9999))+str(self.id)

        self.otp=otp_number

        self.save()