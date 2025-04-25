from . import views
from django.urls import path
from .views import Item_Create,Item_Update,Item_Delete,Item_List

urlpatterns =[
   path('item_list',Item_List.as_view(),name = 'Item_List'),
   path('item_create',Item_Create.as_view(),name = 'Item_Create'),
   path('iten_update/<pk>',Item_Update.as_view(),name = 'Item_Update'), 
   path('item_delete/<pk>',Item_Delete.as_view(),name = 'Item_Delete'),
]