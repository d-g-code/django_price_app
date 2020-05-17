from django.urls import path
from . import views

app_name = 'product_price'
urlpatterns = [
    path('', views.index_product, name='index_product'),
    path('signup', views.signup, name='signup'),
    path('add', views.add_product, name='add_product'),
]
