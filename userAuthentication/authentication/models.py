from django.db import models

# Create your models here.

from django.contrib.auth.models import User


class PhoneNumber(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phoneNumber = models.IntegerField()


class OTPCode(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    otpcode = models.IntegerField()
