from django.shortcuts import render
from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.views import View
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

from .models import CustomUser, Customer
from .forms import CustomUserForm, CustomerUserForm

# Create your views here.
class CustomerSignUpView(View):
    form = CustomUserForm
    customeruser_form = CustomerUserForm
    template_name = 'signup.html'

    def post(self, request, *args, **kwargs):
        customuser_form = CustomUserForm(request.POST, prefix='customuser')
        customeruser_form = CustomerUserForm(request.POST, prefix='customeruser')

        # TODO: Form and info DOES NOT SAVE
        if customuser_form.is_valid() and customeruser_form.is_valid():
            uform = customuser_form.save()
            cuform = customeruser_form.save(commit=False)
            cuform.custom_user = uform
            cuform.save()


        # TODO: figure out a way with this
        return HttpResponseRedirect("home")

    def get(self, request):
        form = CustomUserForm
        customeruser_form = CustomerUserForm
        return render(request, 'signup.html', {'form': form, 'customeruser_form': customeruser_form})
