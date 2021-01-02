from django.urls import path

from .views import CustomerSignUpView, EmployeeAddView, UserLoginView

urlpatterns = [
               path("login", UserLoginView.as_view(), name="final_login"),
               path("signup", CustomerSignUpView.as_view(), name="customer_signup"),
               path("add_employee", EmployeeAddView.as_view(), name="employee_add"),
]
