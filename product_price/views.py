from django.shortcuts import render
from .models import Product, Store, Kind
from django.contrib.auth.forms import UserCreationForm
from .forms import AddProductForms
from django.contrib import messages
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import StoreSerializer, KindSerializer, ProductSerializer


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


@api_view(['GET'])
def store_collection(request):
    if request.method == 'GET':
        stores = Store.objects.all()
        print(stores)
        serializer = StoreSerializer(stores, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def kind_collection(request):
    if request.method == 'GET':
        kind = Kind.objects.all()
        serializer = KindSerializer(kind, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def product_collection(request):
    if request.method == 'GET':
        product = Product.objects.all()
        serializer = ProductSerializer(product, many=True)
        print(product)
        return Response(serializer.data)