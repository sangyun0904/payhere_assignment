from django.db import models

# Create your models here.
class Seller(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=255)

class Product(models.Model):
    category = models.CharField(max_length=100)
    price = models.IntegerField()
    origin_price = models.IntegerField()
    name = models.CharField(max_length=100)
    info = models.CharField(max_length=300)
    barcode = models.CharField(max_length=100)
    expire = models.DateTimeField(auto_now_add=True)
    big_size = models.BooleanField(default=False)
