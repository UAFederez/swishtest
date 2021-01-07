from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

from .models import Orders
from .forms import BaseOrderForm, WalkInUserForm, WalkInCustomerForm

# Create your views here.
class OrderListView(ListView):
    model = Orders
    template_name = "orders.html"


class OrderCreateView(View):
    template_name = "order_new.html"

    def post(self, request, *args, **kwargs):
        if request.user.is_customer:
            baseorder_form = BaseOrderForm(request.POST, prefix="baseorder_form")

            if baseorder_form.is_valid():
                order_form = baseorder_form.save(commit=False)
                order_form.customer = request.user.customer
                order_form.status = 1

                # FILLER VALUES
                order_form.delivery_price = 128
                order_form.service_price = 50
                order_form.weight = 2

                order_form.save()

                return HttpResponseRedirect(reverse_lazy('home'))

            else:
                return render(request, 'order_new.html', {'baseorder_form': baseorder_form})


    def get(self, request):
        if request.user.is_customer:
            baseorder_form = BaseOrderForm(prefix="baseorder_form")
            return render(request, 'order_new.html', {'baseorder_form': baseorder_form})
