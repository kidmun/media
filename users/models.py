from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name=models.CharField(max_length=True)
    username=models.CharField(max_length=200, null=True, blank=True)
    email=models.EmailField(max_length=200)
    location=models.CharField(max_length=200, null=True, blank=True)
    bio=models.TextField(max_length=200, null=True, blank=True)
    job=models.CharField(max_length=200, null=True, blank=True)
    status=models.CharField(max_length=200, null=True, blank=True)
    profile=models.ImageField(null=True, blank=True,)

