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
    template_name = 'signup.html'

    def post(self, request, *args, **kwargs):
        customuser_form = CustomUserForm(request.POST, prefix='customuser_form')
        customeruser_form = CustomerUserForm(request.POST, prefix='customeruser_form')

        if customuser_form.is_valid() and customeruser_form.is_valid():
            uform = customuser_form.save(commit=False)
            uform.is_customer = True
            uform.save()

            cuform = customeruser_form.save(commit=False)
            cuform.custom_user = uform
            cuform.save()

            return HttpResponseRedirect(reverse_lazy('home'))

    def get(self, request):
        customuser_form = CustomUserForm(prefix='customuser_form')
        customeruser_form = CustomerUserForm(prefix='customeruser_form')
        return render(request, 'signup.html', {'customuser_form': customuser_form, 'customeruser_form': customeruser_form})
