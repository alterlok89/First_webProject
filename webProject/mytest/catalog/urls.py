from django.urls import path
from . import views


urlpatterns = [
    path('', views.ProductListViews.as_view(), name='index'),
    path('home', views.ProductListViews.as_view(), name='index'),
    path('cart', views.cart, name='cart'),
    path('login-register', views.login_register, name='login-register'),
    path('checkout', views.checkout, name='checkout'),
    path('contact', views.contact, name='contact'),
    path('shop', views.shop, name='shop'),
    path('product-details', views.product_details, name='product-details'),
    path('wishlist', views.wishlist, name='wishlist'),
    ]
