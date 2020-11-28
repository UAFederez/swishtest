from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Orders

# Create your views here.
class OrderListView(ListView):
    model = Orders
    template_name = "home.html"
