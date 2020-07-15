from django.shortcuts import render
from .models import Product, Store
from django.contrib.auth.forms import UserCreationForm
from .forms import AddProductForms
from django.contrib import messages


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


def add_product(request):
    form = AddProductForms(request.POST or None)
    if form.is_valid():
        form.save()
        form = AddProductForms()
        messages.success(request, f'Artykuł dodany')
        return render(request, 'product_price/add_product.html', {'form': form})
    return render(request, 'product_price/add_product.html', {'form': form})
