from django import forms

from .models import Orders
from custom_user.models import CustomUser, Customer


class BaseOrderForm(forms.ModelForm):

    class Meta:
        model = Orders
        fields = ('type', 'service', 'address', 'pickup_time',)


class WalkInUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name')


class WalkInCustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('contact',)
