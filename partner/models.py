from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Partner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(
        max_length=50,
        verbose_name="Company Name",
    )
    contact = models.CharField(
        max_length=50,
        verbose_name="Contact Number",
    )
    address = models.CharField(
        max_length=200,
        verbose_name= "Company Address",
    )
    description = models.TextField(
        max_length=200,
        verbose_name="Company Description",
    )
