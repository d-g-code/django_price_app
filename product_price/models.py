from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=40)
    price = models.DecimalField(max_digits=5, decimal_places=2, default='')
    store = models.CharField(max_length=20, default='')

    def __str__(self):
        return self.name


