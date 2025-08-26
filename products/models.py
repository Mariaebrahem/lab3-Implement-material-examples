
from django.db import models

class  products(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    description = models.TextField()
    # image = models.ImageField(upload_to='product_image/%y/%m/%d')
    active = models.BooleanField(default=True)
