from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid


# Create your models here.
class CustomUser(AbstractUser):
    username = models.CharField(max_length=100, blank=True, unique=True, default=uuid.uuid4)
    email = models.EmailField(max_length=254, blank=True, unique=True)
    first_name = models.CharField(max_length=20, null=False)
    last_name = models.CharField(max_length=20, null=False)
    is_customer = models.BooleanField(default=False)
    is_employee = models.BooleanField(default=False)


class Customer(models.Model):
    custom_user = models.OneToOneField(CustomUser,
                                       on_delete=models.CASCADE,
                                       primary_key=True)
    contact = models.CharField(max_length=20)
    saved_address = models.CharField(max_length=100, blank=True)


class Employee(models.Model):
    custom_user = models.OneToOneField(CustomUser,
                                       on_delete=models.CASCADE,
                                       primary_key=True)
    start_date = models.DateField()
