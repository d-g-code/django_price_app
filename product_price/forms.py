from django import forms
from .models import Product


class AddProductForms(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product', 'price', 'product_store']
