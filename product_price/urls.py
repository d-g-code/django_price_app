from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'product_price'
urlpatterns = [
    path('', views.index_product, name='index_product'),
    path('signup', views.signup, name='signup'),
    path('search_form', views.search_form, name='search_form'),
    path('add', views.add_product, name='add_product'),
    path('login/', auth_views.LoginView.as_view(
        template_name='product_price/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(
        template_name='product_price/logout.html'), name='logout'),
]
