#from typing import Any from django.forms import BaseModelFormfrom django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from .models import Customer
from .forms import Customer_Form
from django.views.generic import  CreateView,UpdateView,DeleteView,ListView
#from django.contrib.auth.views import LoginView,LogoutView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class Customer_Create(LoginRequiredMixin,CreateView):
        model = Customer
        #fields ='__all__'
        form_class=Customer_Form
        login_url ='login'
        success_url = '/'

        def get(self, request, *args, **kwargs):
                return super().get(request, *args, **kwargs)
        
        def form_valid(self, form):
                messages.success(self.request,'New Customer Successfully Created')
                return super().form_valid(form)
        

class Customer_List(LoginRequiredMixin,ListView):
        model = Customer
        fields='__all__'
        context_object_name='customers'
        #success_url = '/customer_create'
        login_url ='login'
 
class Customer_Update(LoginRequiredMixin,UpdateView):
        model = Customer
        #fields ='__all__'
        form_class=Customer_Form
        success_url = '/'


        def form_valid(self, form):
                messages.success(self.request,f'Customer  {form.instance.Name}   Was Successfully Updated')
                return super().form_valid(form)


class Customer_Delete(LoginRequiredMixin,DeleteView):
        model = Customer
        success_url = '/'



