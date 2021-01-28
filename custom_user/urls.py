from django.urls import path

from .views import CustomerSignUpView, EmployeeAddView, UserLoginView, CustomerEditProfileView

urlpatterns = [
               path("login", UserLoginView.as_view(), name="final_login"),
               path("edit_customer_profile", CustomerEditProfileView.as_view(), name="customer_edit_profile"),
               path("signup", CustomerSignUpView.as_view(), name="customer_signup"),
               path("add_employee", EmployeeAddView.as_view(), name="employee_add"),
]
