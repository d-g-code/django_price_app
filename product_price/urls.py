from django.urls import path
from . import views

app_name = 'product_price'
urlpatterns = [
    path('', views.index_product, name='index_product'),
]
