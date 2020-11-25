from django import forms
from .models import Product, Store, Kind


class AddProductForms(forms.ModelForm):
    product = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-group', 'placeholder': 'product'}))
    price = forms.DecimalField(widget=forms.TextInput(
        attrs={'class': 'form-group', 'placeholder': 'price', 'type': 'number', 'step': 0.01, 'min': 0}))
    product_kind = forms.ModelChoiceField(queryset=Kind.objects.all())
    product_store = forms.ModelChoiceField(queryset=Store.objects.all())

    class Meta:
        model = Product
        fields = ['product', 'price', 'product_kind', 'product_store']
