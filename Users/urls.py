from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView 

urlpatterns = [
    path('login',views.sign_in,name='login'),
    path('logout/', views.sign_out,name='logout'),
]