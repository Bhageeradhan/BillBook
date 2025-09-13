from django.db import models


class Product(models.Model):
    product_name = models.CharField(max_length=100, null=True)
    product_code = models.CharField(max_length=50, null=True)
    price = models.FloatField(default=0)
    tax = models.IntegerField(default=0)
    picture = models.ImageField(null=True, upload_to='imgaes/')

    def __str__(self):
        return self.product_name
