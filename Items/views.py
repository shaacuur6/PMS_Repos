#from typing import Any from django.forms import BaseModelFormfrom django.http import HttpRequest, HttpResponsefrom django.shortcuts import render
from .models import Item
from django.views.generic import  CreateView,UpdateView,DeleteView,ListView
#from django.contrib.auth.views import LoginView,LogoutView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class Item_Create(LoginRequiredMixin,CreateView):
        model = Item
        fields ='__all__'
        
        #form_class=Customer_Form
        login_url ='login'
        success_url = '/'

        
        def form_valid(self, form):
                messages.success(self.request,'New Item Created Successfully')
                return super().form_valid(form)
        

class Item_List(LoginRequiredMixin,ListView):
        model = Item
        fields='__all__'
        context_object_name='items'
        #success_url = '/customer_create'
        login_url ='login'
 
class Item_Update(LoginRequiredMixin,UpdateView):
        model = Item
        fields ='__all__'
        #form_class=Customer_Form
        success_url = '/item_list'


        def form_valid(self, form):
                messages.success(self.request,f'Item  {form.instance.item_name},   Was Successfully Updated')
                return super().form_valid(form)


class Item_Delete(LoginRequiredMixin,DeleteView):
        model = Item
        success_url = '/'



