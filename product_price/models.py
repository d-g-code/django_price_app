from django.db import models
from django.utils import timezone


class Store(models.Model):
    store = models.CharField(max_length=10, default='')

    def __str__(self):
        return self.store


class Kind(models.Model):
    kind = models.CharField(max_length=10, default='')

    def __str__(self):
        return self.kind


class Product(models.Model):
    product = models.CharField(max_length=40, default='')
    price = models.DecimalField(max_digits=7, decimal_places=2, default='')
    product_kind = models.ForeignKey(Kind, on_delete=models.CASCADE)
    product_store = models.ForeignKey(Store, on_delete=models.  CASCADE)
    product_data = models.DateTimeField(timezone.now(), default=timezone.now())

    def __str__(self):
        return self.product
