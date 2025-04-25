from . import views
from django.urls import path
from .views import Item_Category_Create,Item_Category_Update,Item_Category_Delete,Item_Category_List

urlpatterns =[
   path('category_list',Item_Category_List.as_view(),name = 'Category_List'),
   path('category_create',Item_Category_Create.as_view(),name = 'Category_Create'),
   path('category_update/<pk>',Item_Category_Update.as_view(),name = 'Category_Update'), 
   path('category_delete/<pk>',Item_Category_Delete.as_view(),name = 'Category_Delete'),
]