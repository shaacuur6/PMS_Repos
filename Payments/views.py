from django.shortcuts import render
from .models import Payment
from django.views.generic import  CreateView,UpdateView,DeleteView,ListView
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class Payment_Create(LoginRequiredMixin,CreateView):
        model = Payment
        fields ='__all__'
        #form_class=Customer_Form
        login_url ='login'
        success_url = '/'

class Payment_List(LoginRequiredMixin,ListView):
        model = Payment
        fields='__all__'
        #success_url = '/customer_create'
        login_url ='login'
 
class Payment_Update(LoginRequiredMixin,UpdateView):
        model = Payment
        fields ='__all__'
        #form_class=Customer_Form
        login_url ='login'
        success_url = '/Payment_List'

class Payment_Delete(DeleteView):
        model = Payment
        success_url = '/'



