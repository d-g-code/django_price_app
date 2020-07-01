from django.shortcuts import render, HttpResponseRedirect, reverse
from .models import Product
from django.contrib.auth.forms import UserCreationForm
from .forms import AddProductForms
from django.contrib import messages


def index_product(request):
    all_products = Product.objects.order_by('name')
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



# https://www.digitalocean.com/community/tutorials/how-to-create-a-django-app-and-connect-it-to-a-database
# https://www.mycli.net/config
