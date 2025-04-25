from . import views
from django.urls import path
from .views import Payment_Create,Payment_Update,Payment_Delete,Payment_List

urlpatterns =[
   path('Payment_List',Payment_List.as_view(),name = 'Payment_List'),
   path('Payment_Create',Payment_Create.as_view(),name = 'Paymemt_Create'),
   path('Payment_Update/<pk>',Payment_Update.as_view(),name = 'Payment_Update'), 
   path('',Payment_Delete.as_view(),name = 'Payment_Delete'),
]