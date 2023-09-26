from django.shortcuts import render,redirect

from carts.models import Cart
from products.models import Product

# Create your views here.

def addToCart(request):
    if request.method=='POST':
        productId=request.POST['productId']
        productQty=request.POST['productQty']
    print(productId,productQty,request.user.id)
    cart = Cart(UserId=request.user.id ,ProductId=productId,Quantity=productQty)
    cart.save()
    return redirect('products:productList')

def cartList(request):
    cart_items = Cart.objects.filter(UserId=request.user.id).values('ProductId', 'Quantity')
    #product_ids = [item['ProductId'] for item in cart_items]
    product_quantity_map = {item['ProductId']: item['Quantity'] for item in cart_items}
    product_ids = list(product_quantity_map.keys())
    matching_products = Product.objects.filter(id__in=product_ids)
    TotalPrice =0
    for product in matching_products:
        product.quantity = product_quantity_map.get(product.id, 0)
        product.itemTotal = product.quantity*product.Price
        TotalPrice +=product.quantity*product.Price
    print(TotalPrice)
    return render(request,'cart.html',{"cartItems":matching_products,"TotalPrice":TotalPrice})

def removeFromCart(request,productId):
    cartProduct = Cart.objects.filter(UserId=request.user.id, ProductId=productId)
    cartProduct.first().delete()
    return redirect('carts:cartList')