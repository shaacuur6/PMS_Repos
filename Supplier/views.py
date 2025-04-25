#from typing import Any from django.forms import BaseModelFormfrom django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from .models import Supplier
from .forms import Supplier_Form
from django.views.generic import  CreateView,UpdateView,DeleteView,ListView
#from django.contrib.auth.views import LoginView,LogoutView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class Supplier_Create(LoginRequiredMixin,CreateView):
        model = Supplier
        #fields ='__all__'
        form_class=Supplier_Form
        login_url ='login'
        success_url = '/supplier_list'

        def get(self, request, *args, **kwargs):
                return super().get(request, *args, **kwargs)
        
        def form_valid(self, form):
                messages.success(self.request,'New Supplier Successfully Created')
                return super().form_valid(form)
        

class Supplier_List(LoginRequiredMixin,ListView):
        model = Supplier
        fields='__all__'
        context_object_name='suppliers'
        #success_url = '/customer_create'
        login_url ='login'
 
class Supplier_Update(LoginRequiredMixin,UpdateView):
        model = Supplier
        #fields ='__all__'
        form_class=Supplier_Form
        success_url = '/supplier_list'


        def form_valid(self, form):
                messages.success(self.request,f'Supplier  {form.instance.Name}   Was Successfully Updated')
                return super().form_valid(form)


class Supplier_Delete(LoginRequiredMixin,DeleteView):
        model =  Supplier
        success_url = '/supplier_list'



