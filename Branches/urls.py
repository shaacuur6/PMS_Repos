from . import views
from django.urls import path
from .views import Branch_Create,Branch_Update,Branch_Delete,Branch_List

urlpatterns =[
   path('branch_list',Branch_List.as_view(),name = 'branch_list'),
   path('branch_create',Branch_Create.as_view(),name = 'branch_create'),
   path('branch_update/<pk>',Branch_Update.as_view(),name = 'branch_update'), 
   path('branch_delete/<pk>',Branch_Delete.as_view(),name = 'branch_delete'),
]