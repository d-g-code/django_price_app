from django.shortcuts import render, get_object_or_404
from .models import Product
from django.http import Http404


def index_product(request):
    all_products = Product.objects.all()
    return render(request, 'product_price/product.html', {'all_products': all_products})

