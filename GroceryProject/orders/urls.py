from django.urls import path
from . import views

app_name = 'orders'
urlpatterns = [
    path('createOrder/', views.createOrder,name="createOrder"),
    path('orderList/',views.orderList,name="orderList")
]