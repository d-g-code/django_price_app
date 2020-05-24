from django import forms
from .models import Product
from django.contrib.auth.forms import UserCreationForm


class AddProductForms(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'store']


class SearchForm(forms.Form):
    q = forms.CharField(
            label='Search',
            widget=forms.TextInput(attrs={'placeholder': 'Search'})
        )


class MyUserCreationForm(UserCreationForm):
    username = forms.CharField(
        label='username',
        widget=forms.TextInput(attrs={'placeholder': 'Username'})
    )
    password = forms.CharField(
        label='password',
        widget=forms.TextInput(attrs={'placeholder': 'Password'})
    )
