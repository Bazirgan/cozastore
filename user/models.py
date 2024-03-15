from django.db import models

from django.contrib.auth.models import AbstractUser


class MyUser(AbstractUser):
    phone = models.CharField(max_length=15,unique=True)
    adress = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    date_of_brith = models.DateField(null=True, blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)