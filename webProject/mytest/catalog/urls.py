from django.urls import path, re_path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.home, name='index'),
    path('cart', views.cart, name='cart'),
    path('login-register', views.RegisterUser.as_view(), name='login-register'),
    path('checkout', views.checkout, name='checkout'),
    path('contact', views.contact, name='contact'),
    path('product-details/<slug:prod_slug>/', views.ProductDetail.as_view(), name='product-details'),
    path('wishlist', views.wishlist, name='wishlist'),
    path('shop/', views.Shop.as_view(), name='shop'),
    path('shop/<slug:cat_slug>', views.ShopCategory.as_view(), name='category'),
    ]
