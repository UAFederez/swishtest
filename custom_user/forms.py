from django import forms
from django.db import transaction

from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser, Customer

class CustomerUserForm(forms.ModelForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name',)


class CustomerCreationForm(CustomerUserForm):

    contact = forms.CharField(widget=forms.TextInput())

    class Meta(CustomerUserForm.Meta):
        model = CustomUser

        fields = CustomerUserForm.Meta.fields + ('contact',)

    @transaction.atomic
    def save(self):
        user = super.save(commit=False)
        user.is_customer = True
        user.save()
        customer = Customer.objects.create(custom_user=user, contact=contact)


# class CustomerChangeForm(UserChangeForm):
#
#     contact = forms.CharField()
#
#     class Meta(UserChangeForm):
#         class Meta:
#             model = CustomUser
#             fields = ("username", "email", "contact",)
