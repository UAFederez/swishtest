from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse

from .models import Orders

# Create your views here.
class OrderListView(ListView):
    model = Orders
    template_name = "orders.html"


class OrderCreateView(CreateView):
    model = Orders
    template_name = "order_new.html"
    fields = ("ref_id", "customer")

    def get_success_url(self):
        return reverse('home')
