from django.db import models


# Create your models here.
class Orders(models.Model):
    ref_id = models.IntegerField(primary_key=True)
    customer = models.CharField(max_length=50)
    order_time = models.DateTimeField(auto_now_add=True)
    pickup_time = models.DateTimeField(null=True, blank=True)
