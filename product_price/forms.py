from django import forms
from .models import Product
from django.contrib.auth.forms import UserCreationForm


class AddProductForms(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'store']


class MyUserCreationForm(UserCreationForm):
    username = forms.CharField(
        label='username',
        widget=forms.TextInput(attrs={'placeholder': 'Username'})
    )
    password1 = forms.CharField(
        label='password1',
        widget=forms.TextInput(attrs={'placeholder': 'Password1'})
    )
    password2 = forms.CharField(
        label='password2',
        widget=forms.TextInput(attrs={'placeholder': 'Password2'})
    )
