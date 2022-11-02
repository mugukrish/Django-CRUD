from django.db import models

# Create your models here.

class ProductModel(models.Model):
    productname = models.CharField(max_length=50)
    price = models.DecimalField(null=True, max_digits=100, decimal_places=2)


