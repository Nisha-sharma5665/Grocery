from django.shortcuts import render
from .models import Product
from .common import GetOptionValueFromID
# Create your views here.
def productList(request):
    productList = Product.objects.all()
    for product in productList:
        product.Type= GetOptionValueFromID(product.Type)
    print(productList)
    return render(request,'listing.html',{"ProductList":productList})

def productDetail(request):
    return render(request,'detail.html')
