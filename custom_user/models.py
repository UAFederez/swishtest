from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class CustomUser(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_employee = models.BooleanField(default=False)


class Customer(models.Model):
    custom_user = models.OneToOneField(User,
                                       on_delete=models.CASCADE,
                                       primary_key=True)
    contact = models.CharField(max_length=20)
