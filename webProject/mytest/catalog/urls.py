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
    re_path(r'^product-details/(?P<id>\d+)$', views.product_details, name='product-details'),
    # path('product-details', views.product_details, name='product-details'),
    path('wishlist', views.wishlist, name='wishlist'),
    path('shop/', views.ProductListViews.as_view(), name='shop'),
    path('shop/marvel', views.MarvelListViews.as_view(), name='shop_marvel'),
    path('shop/dc_comics', views.DccomicsListViews.as_view(), name='shop_dc_comics'),
    path('shop/disney', views.DisneyListViews.as_view(), name='shop_disney'),
    path('shop/games', views.GamesListViews.as_view(), name='shop_games'),
    path('shop/icons', views.IconsListViews.as_view(), name='shop_icons'),
    path('shop/sport', views.SportListViews.as_view(), name='shop_sport'),
    path('shop/anime', views.AnimeListViews.as_view(), name='shop_anime'),
    path('shop/music', views.MusicListViews.as_view(), name='shop_music'),
    path('shop/mult', views.MultListViews.as_view(), name='shop_mult'),
    path('shop/film', views.FilmListViews.as_view(), name='shop_film'),
    path('shop/serials', views.SerialsListViews.as_view(), name='shop_serials'),
    ]
