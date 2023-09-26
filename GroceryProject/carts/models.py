from django.db import models

# Create your models here.

class Cart(models.Model):
    UserId = models.IntegerField()
    ProductId = models.IntegerField()
    Quantity = models.IntegerField()
    def __str__(self):
        return self.id
