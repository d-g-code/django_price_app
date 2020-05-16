from django.shortcuts import render, redirect
from .models import Product
from django.contrib.auth.forms import UserCreationForm


def index_product(request):
    all_products = Product.objects.all()
    return render(request, 'product_price/product.html', {'all_products': all_products})


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'product_price/product.html')
    else:
        form = UserCreationForm()
        return render(request, 'product_price/signup.html', {'form': form})

