from django.shortcuts import render

# Create your views here.
from django.views import generic
from .models import Product


def index(request):
    products = Product.objects.all()
    print(products)
    print(f'-----\n{request}\n-----')
    return render(request, 'index.html', {"products": products})


def cart(request):
    print(f'-----\n{request}\n-----')
    return render(request, 'cart.html')


def categories(request):
    print(f'-----\n{request}\n-----')
    return render(request, 'categories.html')


def checkout(request):
    print(f'-----\n{request}\n-----')
    return render(request, 'checkout.html')


def contact(request):
    print(f'-----\n{request}\n-----')
    return render(request, 'contact.html')


def product(request):
    print(f'-----\n{request}\n-----')
    return render(request, 'product.html')


def home(request):
    print(f'-----\n{request}\n-----')
    return render(request, 'index.html')


class ProductListViews(generic.ListView):
    model = Product
    template_name = 'base.html'
    context_object_name = 'product_list'
