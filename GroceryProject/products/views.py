from django.shortcuts import render,get_object_or_404

from carts.models import Cart
from .models import Product
from .common import GetOptionValueFromID
# Create your views here.
def productList(request):
    productList = Product.objects.all()
    for product in productList:
        product.Type= GetOptionValueFromID(product.Type)
    print(productList)
    return render(request,'listing.html',{"ProductList":productList})

def productDetail(request,product_id):
    product = get_object_or_404(Product, pk=product_id)
    product.Type=GetOptionValueFromID(product.Type)
    product.ExistInCart = Cart.objects.filter(UserId=request.user.id,ProductId=product_id).exists()
    print(product)
    return render(request,'detail.html',{"product":product})
