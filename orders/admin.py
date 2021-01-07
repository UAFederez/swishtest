from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Orders

# Register your models here.
class OrdersAdmin(admin.ModelAdmin):
    list_display = ('ref_id', 'get_customer', 'status', 'order_time', 'service_price')

    def get_customer(self, obj):
        return obj.customer.custom_user.first_name + " " + obj.customer.custom_user.last_name

    get_customer.short_description = 'Customer'
    get_customer.admin_order_field = 'customer__name'

admin.site.register(Orders, OrdersAdmin)
