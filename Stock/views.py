#from typing import Any from django.forms import BaseModelFormfrom django.http import HttpRequest, HttpResponsefrom django.shortcuts import render
from .models import Stock
from django.views.generic import  CreateView,UpdateView,DeleteView,ListView
#from django.contrib.auth.views import LoginView,LogoutView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class Stock_Create(LoginRequiredMixin,CreateView):
        model = Stock
        fields ='__all__'
        #fields=['item','item_qty','item_price','branch']
        #form_class=Customer_Form
        login_url ='login'
        success_url = '/'

        
        def form_valid(self, form):
                messages.success(self.request,'New Stock Created Successfully')
                return super().form_valid(form)
        

class Stock_List(LoginRequiredMixin,ListView):
        model = Stock
        fields='__all__'
        context_object_name='stocks'
        #success_url = '/customer_create'
        login_url ='login'
 
class Stock_Update(LoginRequiredMixin,UpdateView):
        model = Stock
        fields ='__all__'
        #form_class=Customer_Form
        success_url = '/stock_list'


        def form_valid(self, form):
                messages.success(self.request,f'Item  {form.instance.item} was Successfully Updated in Stock')
                return super().form_valid(form)


class Stock_Delete(LoginRequiredMixin,DeleteView):
        model = Stock
        success_url = '/'



