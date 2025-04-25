#from typing import Any from django.forms import BaseModelFormfrom django.http import HttpRequest, HttpResponsefrom django.shortcuts import render
from .models import Branch
from django.views.generic import  CreateView,UpdateView,DeleteView,ListView
#from django.contrib.auth.views import LoginView,LogoutView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class Branch_Create(LoginRequiredMixin,CreateView):
        model = Branch
        fields ='__all__'
        login_url ='login'
        success_url = '/'

        
        def form_valid(self, form):
                messages.success(self.request,'New Branch Successfully Created')
                return super().form_valid(form)
        

class Branch_List(LoginRequiredMixin,ListView):
        model = Branch
        fields='__all__'
        #success_url = '/customer_create'
        login_url ='login'
 
class Branch_Update(LoginRequiredMixin,UpdateView):
        model = Branch
        fields ='__all__'
        #form_class=Customer_Form
        success_url = '/'


        def form_valid(self, form):
                messages.success(self.request,f'Branch  {form.instance.Name},   Was Successfully Updated')
                return super().form_valid(form)


class Branch_Delete(LoginRequiredMixin,DeleteView):
        model = Branch
        success_url = '/'



