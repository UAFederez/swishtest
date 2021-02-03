from django.urls import path

from .views import OrderListView, OrderCreateView, CustomerSearchView

urlpatterns = [
               path("", OrderListView.as_view(), name="order_view"),
               path("new", OrderCreateView.as_view(), name="order_new"),
               path("search_customer", CustomerSearchView.as_view(), name="search_customer")
]
