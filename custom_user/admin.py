from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomerCreationForm
from .models import CustomUser, Customer

# Register your models here.
class CustomerInline(admin.StackedInline):
    model = Customer
    can_delete = False
    verbose_name_plural = "customer"

class CustomerUserAdmin(UserAdmin):
    add_form = CustomerCreationForm
    inlines = (CustomerInline,)

admin.site.register(CustomUser, CustomerUserAdmin)
