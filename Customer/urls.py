from . import views
from django.urls import path
from .views import Customer_Create,Customer_Update,Customer_Delete,Customer_List

urlpatterns =[
   path('',Customer_List.as_view(),name = 'Customer_List'),
   path('customer_create',Customer_Create.as_view(),name = 'Customer_Create'),
   path('customer_update/<pk>',Customer_Update.as_view(),name = 'Customer_Update'), 
   path('customer_delete/<pk>',Customer_Delete.as_view(),name = 'Customer_Delete'),
]