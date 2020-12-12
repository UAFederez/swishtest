from django.shortcuts import render
from django.contrib.auth import login
from django.shortcuts import redirect
from django.views.generic import CreateView

from .models import CustomUser, Customer

# Create your views here.
class CustomerSignUpView(CreateView):
    model = CustomUser
    form_class = CustomerCreationForm
    template_name = "signup.html"

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'student'
        return super().get_context_data(**kwargs)
