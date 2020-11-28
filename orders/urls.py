from django.urls import path

from .views import OrderListView, OrderCreateView

urlpatterns = [
               path("", OrderListView.as_view(), name="home"),
               path("orders/new", OrderCreateView.as_view(), name="order_new")
]
