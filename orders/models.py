from django.db import models
import uuid


class OrderStatus():
    STATUS_CANCELLED = 0
    STATUS_FETCH = 1
    STATUS_RECEIVED = 2
    STATUS_CONFIRMED = 3
    STATUS_PROCESSING = 4
    STATUS_READY = 5
    STATUS_GIVEN = 6

    STATUS_CHOICES = (
                      (STATUS_CANCELLED, 'Cancelled'),
                      (STATUS_FETCH, 'Fetch'),
                      (STATUS_RECEIVED, 'Received'),
                      (STATUS_CONFIRMED, 'Confirmed'),
                      (STATUS_PROCESSING, 'Processing'),
                      (STATUS_READY, 'Ready'),
                      (STATUS_GIVEN, 'Given')
    )


class OrderService():
    SERVICE_WD = 0
    SERVICE_WDF = 1
    SERVICE_DC = 2

    SERVICE_CHOICES = (
                       (SERVICE_WD, 'Wash and Dry'),
                       (SERVICE_WDF, 'Wash, Dry, and Fold'),
                       (SERVICE_DC, 'Dry Cleaning')
    )



class OrderType():
    TYPE_DELIVERY = 0
    TYPE_PICKUP = 1

    TYPE_CHOICES = (
                    (TYPE_DELIVERY, 'Delivery'),
                    (TYPE_PICKUP, 'Pick-up')
    )


# Create your models here.
class Orders(models.Model):
    def generate_id():
        return uuid.uuid4().hex[:6].upper()

    ref_id = models.CharField(max_length=6, primary_key=True, unique=True, default=generate_id)
    customer = models.ForeignKey('custom_user.Customer', on_delete=models.SET_NULL, null=True)

    type = models.IntegerField(choices=OrderType.TYPE_CHOICES)
    status = models.IntegerField(choices=OrderStatus.STATUS_CHOICES)
    service = models.IntegerField(choices=OrderService.SERVICE_CHOICES)

    address = models.CharField(max_length=100, blank=True)
    order_time = models.DateTimeField(auto_now_add=True)
    pickup_time = models.DateField(null=True, blank=True)

    delivery_price = models.DecimalField(max_digits=6, decimal_places=2)
    service_price = models.DecimalField(max_digits=6, decimal_places=2)
    weight = models.DecimalField(max_digits=6, decimal_places=2)
