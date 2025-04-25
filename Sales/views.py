#from typing import Any from django.forms import BaseModelFormfrom django.http import HttpRequest, HttpResponsefrom django.shortcuts import render
from .models import Sale
from django.views.generic import  CreateView,UpdateView,DeleteView,ListView
#from django.contrib.auth.views import LoginView,LogoutView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class New_Sales(LoginRequiredMixin,CreateView):
        model = Sale
        fields ='__all__'
        #form_class=Customer_Form
        login_url ='login'
        success_url = '/'

        
        def form_valid(self, form):
                messages.success(self.request,'New Sales Created Successfully')
                return super().form_valid(form)
        

class Sales_List(LoginRequiredMixin,ListView):
        model = Sale
        fields='__all__'
        context_object_name='sales'
        success_url = '/sales_list'
        login_url ='login'
 
class Update_Sales(LoginRequiredMixin,UpdateView):
        model = Sale
        fields ='__all__'
        #form_class=Customer_Form
        success_url = '/sales_list'


        def form_valid(self, form):
                messages.success(self.request,f'Sales  {form.instance.item_name},   Was Successfully Updated')
                return super().form_valid(form)


class Delete_Sales(LoginRequiredMixin,DeleteView):
        model = Sale
        success_url = '/'



