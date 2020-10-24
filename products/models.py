from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length = 50)
    description = models.CharField(max_length=120)
    price = models.DecimalField(decimal_places=2, max_digits = 10)
    image = models.ImageField(blank=True, upload_to='images/')

class Order(models.Model):
    productId = models.IntegerField()
    status = models.CharField(max_length=20)

class Constants():
    default = 'Default'
    processing = 'Processing'
    dispatched = 'Dispatched'
    delivered = 'Delivered'
    cancelled = 'Cancelled'