from . import views
from django.urls import path
from .views import Stock_Create,Stock_List,Stock_Update,Stock_Delete

urlpatterns =[
   path('stock_list',Stock_List.as_view(),name = 'Stock_List'),
   path('stock_create',Stock_Create.as_view(),name = 'Stock_Create'),
   path('stock_update/<pk>',Stock_Update.as_view(),name = 'Stock_Update'), 
   path('stock_delete/<pk>',Stock_Delete.as_view(),name = 'Stock_Delete'),
]