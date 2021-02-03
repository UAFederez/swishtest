import uuid
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.db.models import Q


from .models import Orders
from custom_user.models import Customer, CustomUser
from .forms import BaseOrderForm, WalkInUserForm, WalkInCustomerForm

# Create your views here.
class OrderListView(ListView):
    model = Orders
    template_name = "orders.html"

class OrderCreateView(View):
    template_name = "order_new.html"

    def post(self, request, *args, **kwargs):
        customer_uid      = (request.session['uname_create_order_existing'] if 'uname_create_order_existing' in request.session else 0)
        customuser_form   = WalkInUserForm(request.POST, prefix='customuser_form')
        customeruser_form = WalkInCustomerForm(request.POST, prefix='customeruser_form')
        baseorder_form    = BaseOrderForm(request.POST, prefix="baseorder_form")

        if baseorder_form.is_valid():
            order_form = baseorder_form.save(commit=False)
            order_form.status = 1

            if request.user.is_employee or request.user.is_superuser:
                if customer_uid:
                    custom_user         = get_customer_by_uuid(customer_uid)
                    customer            = Customer.objects.get(custom_user = custom_user)
                    order_form.customer = customer
                    del request.session['uname_create_order_existing']
                elif customuser_form.is_valid() and customeruser_form.is_valid():
                    uform = customuser_form.save(commit=False)
                    uform.is_customer = True
                    uform.save()

                    cuform = customeruser_form.save(commit=False)
                    cuform.custom_user = uform
                    cuform.save()

                    order_form.customer = cuform

                else:
                    return render(request, 'order_new.html', {
                                                'baseorder_form':    baseorder_form, 
                                                'customuser_form':   customuser_form, 
                                                'customeruser_form': customeruser_form,
                                                'customer_uuid_opt': 0
                                                })

            elif request.user.is_customer:
                order_form.customer = request.user.customer

            # FILLER VALUES
            order_form.delivery_price = 128
            order_form.service_price = 50
            order_form.weight = 2

            order_form.save()

            return HttpResponseRedirect(reverse_lazy('home'))

        else:
            return render(request, 'order_new.html', {
                                        'baseorder_form':    baseorder_form, 
                                        'customuser_form':   customuser_form, 
                                        'customeruser_form': customeruser_form,
                                        'customer_uuid_opt': 0
                                        })


    def get(self, request, uid = None):
        customer_uid      = (request.session['uname_create_order_existing'] if 'uname_create_order_existing' in request.session else 0)
        customuser_form   = None
        customeruser_form = None

        if request.user.is_employee or request.user.is_superuser:

            if customer_uid:
                print("UID:", customer_uid)
            else:
                customuser_form = WalkInUserForm(prefix='customuser_form')
                customeruser_form = WalkInCustomerForm(prefix='customeruser_form')

        baseorder_form = BaseOrderForm(prefix="baseorder_form")
        return render(request, 'order_new.html', {
                                    'baseorder_form':    baseorder_form, 
                                    'customuser_form':   customuser_form, 
                                    'customeruser_form': customeruser_form,
                                    'customer_uuid_opt': uid
                                    })


class CustomerSearchView(ListView):
    model = CustomUser
    template_name = "search_users.html"

    def get_queryset(self):
        query     = self.request.GET.get('query')
        filter_by = self.request.GET.get('filter')
        if query:
            if filter_by == "name":
                return CustomUser.objects.filter( Q( is_customer          = True ),
                                                  Q( first_name__contains = query) | 
                                                  Q( last_name__contains  = query) )
            else:
                return CustomUser.objects.filter( Q( is_customer     = True ),
                                                  Q( email__contains = query) )

        else:
            return CustomUser.objects.filter( Q( is_customer = True ) )

    def post(self, request):
        username = self.request.POST.get('username')
        request.session['uname_create_order_existing'] = username.strip()
        return HttpResponseRedirect("new")


def get_customer_by_uuid(uuid):
    try:
        return CustomUser.objects.get(username = uuid)
    except CustomUser.DoesNotExist:
        return None

