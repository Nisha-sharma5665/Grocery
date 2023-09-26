from django.urls import path
from . import views

app_name = 'products'
urlpatterns = [
    path('', views.productList,name="productList"),
    path('product/<int:product_id>/', views.productDetail, name='product_detail'),
]