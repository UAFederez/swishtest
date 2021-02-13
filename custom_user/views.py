from django.shortcuts import render
from django.views import View
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm

from .forms import CustomUserForm, CustomerUserForm, EmployeeUserForm, EditUserForm
from .models import CustomUser, Customer

# Create your views here.
class CustomerSignUpView(View):
    template_name = 'signup.html'

    def post(self, request, *args, **kwargs):
        customuser_form = CustomUserForm(request.POST, prefix='customuser_form')
        customeruser_form = CustomerUserForm(request.POST, prefix='customeruser_form')

        if customuser_form.is_valid() and customeruser_form.is_valid():
            uform = customuser_form.save(commit=False)
            password = customuser_form.cleaned_data['password']

            uform.set_password(password)
            uform.is_customer = True

            uform.save()

            cuform = customeruser_form.save(commit=False)
            cuform.custom_user = uform
            cuform.save()

            return HttpResponseRedirect(reverse_lazy('home'))

        else:
            return render(request, 'signup.html', {'customuser_form': customuser_form, 'customeruser_form': customeruser_form})

    def get(self, request):
        customuser_form = CustomUserForm(prefix='customuser_form')
        customeruser_form = CustomerUserForm(prefix='customeruser_form')
        return render(request, 'signup.html', {'customuser_form': customuser_form, 'customeruser_form': customeruser_form})



class EmployeeAddView(View):
    template_name = 'employee_add.html'

    def post(self, request, *args, **kwargs):
        customuser_form = CustomUserForm(request.POST, prefix='customuser_form')
        employeeuser_form = EmployeeUserForm(request.POST, prefix='employeeuser_form')

        if customuser_form.is_valid() and employeeuser_form.is_valid():
            uform = customuser_form.save(commit=False)
            password = customuser_form.cleaned_data['password']

            uform.set_password(password)
            uform.is_employee = True

            uform.save()

            euform = employeeuser_form.save(commit=False)
            euform.custom_user = uform
            euform.save()

            return HttpResponseRedirect(reverse_lazy('home'))

        else:
            return render(request, 'employee_add.html', {'customuser_form': customuser_form, 'employeeuser_form': employeeuser_form})

    def get(self, request):
        customuser_form = CustomUserForm(prefix='customuser_form')
        employeeuser_form = EmployeeUserForm(prefix='employeeuser_form')
        return render(request, 'employee_add.html', {'customuser_form': customuser_form, 'employeeuser_form': employeeuser_form})


class UserLoginView(View):
    def post(self, request, *args, **kwargs):
        email = request.POST['email']
        password = request.POST['password']
        username = get_user(email)
        user = authenticate(username=username, password=password)

        if user is not None:
            print("Not None")
            login(request, user)
            return HttpResponseRedirect(reverse_lazy('home'))

        else:
            print("Invalid")
            return render(request, 'registration/login.html', {'error': True})

    def get(self, request):
        return render(request, 'registration/login.html', {'error': False})

class CustomerEditProfileView(View):
    def post(self, request, *args, **kwargs):
        customer        = get_customer(request.user)
        customer_form   = CustomerUserForm(request.POST, instance = customer)
        customuser_form = EditUserForm(request.POST, instance = request.user)

        if customuser_form.is_valid() and customer_form.is_valid():
            customuser_form.save()
            customer_form.save()

            return HttpResponseRedirect(reverse_lazy('home'))
        else:
            return render(request, 'edit_profile.html', {
                    'customuser_form': customuser_form,
                    'customer_form'  : customer_form,
                })

    def get(self, request):
        customer        = get_customer(request.user)
        customer_form   = CustomerUserForm(instance = customer)
        customuser_form = EditUserForm(instance = request.user)

        return render(request, 'edit_profile.html', {
                'customuser_form': customuser_form,
                'customer_form'  : customer_form,
            })

class EditUserPasswordView(View):
    def post(self, request, *args, **kwargs):
        password_form = PasswordChangeForm(request.user, request.POST)

        if password_form.is_valid():
            password_form.save()
            return HttpResponseRedirect(reverse_lazy('home'))
        else:
            return render(request, 'edit_password.html', {
                    'password_form': password_form
                })

    def get(self, request):
        password_form   = PasswordChangeForm(request.user)

        return render(request, 'edit_password.html', {
                'password_form': password_form
            })

def get_customer(custom_user):
    try:
        return Customer.objects.get(custom_user=custom_user)
    except Customer.DoesNotExist:
        return None

def get_user(email):
    try:
        return CustomUser.objects.get(email=email.lower())
    except CustomUser.DoesNotExist:
        return None
