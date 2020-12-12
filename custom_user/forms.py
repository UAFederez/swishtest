from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser, Customer

class CustomerCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser

        fields = ("username", "email", "contact",)

    @transaction.atomic
    def save(self):
        user = super.save(commit=False)
        user.is_customer = True
        user.save()
        customer = Customer.objects.create(custom_user=user)


class CustomerChangeForm(UserChangeForm):

    class Meta(UserChangeForm):
        class Meta:
            model = CustomUser
            fields = ("username", "email", "contact",)
