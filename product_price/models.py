from django.db import models


class Store(models.Model):
    store = models.CharField(max_length=10, default='')

    def __str__(self):
        return self.store


class Product(models.Model):
    product = models.CharField(max_length=40, default='')
    price = models.DecimalField(max_digits=5, decimal_places=2, default='')
    product_store = models.ForeignKey(Store, on_delete=models.CASCADE, default='')

    def __str__(self):
        return self.product
