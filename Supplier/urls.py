from . import views
from django.urls import path
from .views import Supplier_Create,Supplier_Update,Supplier_Delete,Supplier_List

urlpatterns =[
   path('supplier_list',Supplier_List.as_view(),name = 'Supplier_List'),
   path('supplier_create',Supplier_Create.as_view(),name = 'Supplier_Create'),
   path('supplier_update/<pk>',Supplier_Update.as_view(),name = 'Supplier_Update'), 
   path('supplier_delete/<pk>',Supplier_Delete.as_view(),name = 'Supplier_Delete'),
]