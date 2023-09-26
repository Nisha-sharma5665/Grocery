from datetime import datetime, timedelta
from django.shortcuts import render,redirect

from carts.models import Cart
from orders.models import Order,OrderDetail
from products.models import Product

# Create your views here.
def createOrder(request):
    userCartList = Cart.objects.filter(UserId=request.user.id).values('ProductId', 'Quantity')
    product_quantity_map = {item['ProductId']: item['Quantity'] for item in userCartList}
    product_ids = list(product_quantity_map.keys())
    matching_products = Product.objects.filter(id__in=product_ids)
    TotalPrice=0
    for product in matching_products:
        product.quantity = product_quantity_map.get(product.id, 0)
        TotalPrice +=product.quantity*product.Price
    order= Order(userId=request.user.id,
                 createDate=datetime.now(),
                 deliveryDate=datetime.now()+timedelta(days=3),
                 status=1,
                 price=TotalPrice
                 )
    order.save()
    for cart in userCartList:
        orderDetail = OrderDetail(userid=request.user.id,
                                  orderid=order,
                                  productId=cart['ProductId'],
                                  quanity=cart['Quantity'],
                                  price= matching_products.filter(id=cart['ProductId']).first().Price)
        orderDetail.save()

    Cart.objects.filter(UserId=request.user.id).delete()  #Remove from cart
    return redirect("orders:orderList")

def orderList(request):
    pass

def cancelOrder(request):
    pass
