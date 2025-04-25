#from typing import Any from django.forms import BaseModelFormfrom django.http import HttpRequest, HttpResponsefrom django.shortcuts import render
from .models import Item_Category
from django.views.generic import  CreateView,UpdateView,DeleteView,ListView
#from django.contrib.auth.views import LoginView,LogoutView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class Item_Category_Create(LoginRequiredMixin,CreateView):
        model = Item_Category
        fields ='__all__'
        #form_class=Customer_Form
        login_url ='login'
        success_url = '/'

        
        def form_valid(self, form):
                messages.success(self.request,'New Category Created Successfully')
                return super().form_valid(form)
        

class Item_Category_List(LoginRequiredMixin,ListView):
        model = Item_Category
        fields='__all__'
        context_object_name='category'
        success_url = '/category_list'
        login_url ='login'
 
class Item_Category_Update(LoginRequiredMixin,UpdateView):
        model = Item_Category
        fields ='__all__'
        #form_class=Customer_Form
        success_url = '/category_list'


        def form_valid(self, form):
                messages.success(self.request,f'Category  {form.instance.Category_Name},   Was Successfully Updated')
                return super().form_valid(form)


class Item_Category_Delete(LoginRequiredMixin,DeleteView):
        model = Item_Category
        success_url = '/'



