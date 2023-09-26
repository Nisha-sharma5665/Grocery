from django.urls import path
from . import views

app_name = 'carts'
urlpatterns = [
    path('add/', views.addToCart,name="add"),
    path('carts/', views.cartList,name="cartList"),
    path('remove/<int:productId>', views.removeFromCart,name="removeFromCart"),
]