from . import views
from django.urls import path
from .views import New_Sales,Update_Sales,Delete_Sales,Sales_List

urlpatterns =[
   path('sales_list',Sales_List.as_view(),name = 'Sales_List'),
   path('new_sales',New_Sales.as_view(),name = 'New_Sales'),
   path('update_sales/<pk>',Update_Sales.as_view(),name = 'Update_Sales'), 
   path('delete_sales/<pk>',Delete_Sales.as_view(),name = 'Delete_Sales'),
]