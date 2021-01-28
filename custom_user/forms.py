from django import forms
from django.db import transaction

from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser, Customer, Employee

class CustomUserForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ('email', 'password', 'confirm_password', 'first_name', 'last_name',)
        widgets = {
                   'password': forms.PasswordInput(),
                   'confirm_password': forms.PasswordInput(),
        }


    def clean(self):
        cleaned_data = super(CustomUserForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "password and confirm_password does not match"
            )

class EditCustomerCustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('email',)

class CustomerUserForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = ('contact',)



class EmployeeUserForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = ('start_date',)
