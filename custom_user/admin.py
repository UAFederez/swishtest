from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserForm, CustomerUserForm
from .models import CustomUser, Customer

# Register your models here.
class CustomerInline(admin.StackedInline):
    model = Customer
    can_delete = False
    verbose_name_plural = "customer"


# class EmployeeInline(admin.StackedInline):
#     model = Employee
#     can_delete = False
#     verbose_name_plural = "employee"


class CustomUserAdmin(UserAdmin):
    inlines = (CustomerInline,)
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_customer', 'is_employee')


admin.site.register(CustomUser, CustomUserAdmin)
