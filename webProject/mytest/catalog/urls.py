from django.urls import path
from . import views


urlpatterns = [
    path('cart', views.cart, name='cart'),
    path('categories', views.categories, name='categories'),
    path('checkout', views.checkout, name='checkout'),
    path('contact', views.contact, name='contact'),
    path('product', views.product, name='product'),
    path('', views.home, name='index'),
    path('home', views.home, name='index'),
    ]
