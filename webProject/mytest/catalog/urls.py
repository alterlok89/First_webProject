from django.urls import path, re_path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.home, name='index'),
    path('cart', views.cart, name='cart'),
    path('login-register', views.login_register, name='login-register'),
    path('checkout', views.checkout, name='checkout'),
    path('contact', views.contact, name='contact'),
    # path('shop', views.shop, name='shop'),
    path('product-details/<int:id>/', views.product_details, name='product-details'),
    # path('product-details', views.product_details, name='product-details'),
    path('wishlist', views.wishlist, name='wishlist'),
    path('shop/', views.shop, name='shop'),
    path('shop/<int:cat_id>', views.shop_category, name='category'),
    ]
