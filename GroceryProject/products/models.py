from django.db import models

# Create your models here.
TYPE_CHOICES = (
    ("1", "Fruits"),
    ("2", "Vegetables"),
    ("3", "Dairy"),
    ("4", "Bread"),
    ("5", "Cleaners"),
    ("6", "Paper Goods"),
    ("7", "Personal Care"),
    ("8", "Other"),
)

class Brand(models.Model):
    BrandName=models.CharField(max_length=30)

    def __str__(self):
        return self.BrandName

class Product(models.Model):
    ProductName = models.CharField(max_length=50)
    Price = models.IntegerField()
    BrandName = models.ForeignKey(Brand,on_delete=models.CASCADE)
    Type = models.CharField(
        max_length = 20,
        choices = TYPE_CHOICES,
        default = '1'
        )
    
    def __str__(self):
        return self.ProductName
