from django.shortcuts import render

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


def product_details(request):
    print(f'-----\n{request}\n-----')
    return render(request, 'product-details-sticky-right.html')


def shop(request):
    print(f'-----\n{request}\n-----')
    return render(request, 'shop.html')

def wishlist(request):
    print(f'-----\n{request}\n-----')
    return render(request, 'wishlist.html')



class ProductListViews(generic.ListView):
    model = Product
    template_name = 'index.html'
    context_object_name = 'product_list'
