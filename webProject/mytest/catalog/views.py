from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
from django.views import generic
from .models import Product


def index(request):
    products = Product.objects.all()
    print(products)
    print(f'-----\n{request}\n-----')
    return render(request, 'index.html', {"products": products})


def home(request):
    print(f'-----\n{request}\n-----')
    return render(request, 'index.html')

def cart(request):
    print(f'-----\n{request}\n-----')
    return render(request, 'cart.html')


def login_register(request):
    print(f'-----\n{request}\n-----')
    return render(request, 'login-register.html')


def checkout(request):
    print(f'-----\n{request}\n-----')
    return render(request, 'checkout.html')


def contact(request):
    print(f'-----\n{request}\n-----')
    return render(request, 'contact.html')


def product_details(request, id):
    product = Product.objects.get(id=id)
    print(f'-----\n{product}\n-----')
    print(f'-----\n{request}\n-----')
    return render(request, 'product-details.html', context={'product': product})


def shop(request):
    print(f'-----\n{request}\n-----')
    return render(request, 'shop.html')


def wishlist(request):
    print(f'-----\n{request}\n-----')
    return render(request, 'wishlist.html')


class ProductListViews(generic.ListView):
    model = Product
    paginate_by = 20
    template_name = 'shop.html'
    context_object_name = 'product_list'

    def get_queryset(self):
        return Product.objects.all()


class MarvelListViews(ProductListViews):
    def get_queryset(self):
        return Product.objects.filter(category='Фигурки MARVEL')


class DccomicsListViews(ProductListViews):
    def get_queryset(self):
        return Product.objects.filter(category='Фигурки DC Comics')


class DisneyListViews(ProductListViews):
    def get_queryset(self):
        return Product.objects.filter(category='Фигурки Disney')


class GamesListViews(ProductListViews):
    def get_queryset(self):
        return Product.objects.filter(category='Фигурки из Игр')


class IconsListViews(ProductListViews):
    def get_queryset(self):
        return Product.objects.filter(category='Фигурки Icons')


class AnimeListViews(ProductListViews):
    def get_queryset(self):
        return Product.objects.filter(category='Фигурки из Аниме')


class SportListViews(ProductListViews):
    def get_queryset(self):
        return Product.objects.filter(category='Фигурки из Спорта')


class MusicListViews(ProductListViews):
    def get_queryset(self):
        return Product.objects.filter(category='Фигурки из Музыки')


class MultListViews(ProductListViews):
    def get_queryset(self):
        return Product.objects.filter(category='Фигурки из Мультфильмов')


class FilmListViews(ProductListViews):
    def get_queryset(self):
        return Product.objects.filter(category='Фигурки из Фильмов')


class SerialsListViews(ProductListViews):
    def get_queryset(self):
        return Product.objects.filter(category='Фигурки из Сериалов')
