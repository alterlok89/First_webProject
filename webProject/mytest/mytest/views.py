from django.shortcuts import render

# Create your views here.


def index(request):
    print(f'-----\n{request}\n-----')
    return render(request, 'index.html')


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
