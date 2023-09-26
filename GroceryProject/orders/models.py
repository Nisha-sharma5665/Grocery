from django.db import models

# Create your models here.

STATUS = (
    (1, "Order Placed"),
    (2, "Shipped"),
    (3, "Out For Delivery"),
    (4,"Cancelled")
)

class Order(models.Model):
    userId = models.IntegerField() 			
    createDate = models.DateTimeField()
    deliveryDate = models.DateTimeField()
    status =  models.IntegerField(
        choices = STATUS,
        default = 1
        )
    price = models.IntegerField()
    
    def __str__(self):
        return str(self.id)
    
class OrderDetail(models.Model):  
    userid	=models.IntegerField()
    orderid	=models.ForeignKey(Order,on_delete=models.CASCADE)
    productId	=models.IntegerField()
    quanity=models.IntegerField()
    price = models.IntegerField()
    def __str__(self):
        return str(self.id)




    


