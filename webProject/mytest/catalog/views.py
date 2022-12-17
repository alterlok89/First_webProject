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
    return render(request, 'registration/login.html')


def checkout(request):
    print(f'-----\n{request}\n-----')
    return render(request, 'checkout.html')


def contact(request):
    print(f'-----\n{request}\n-----')
    return render(request, 'contact.html')


def product_details(request, id):
    product = Product.objects.get(id=id)
    visits = request.session.get('visits', 0)
    request.session['visits'] = visits + 1
    print(f'-----\n{product}\n-----')
    print(f'-----\n{request}\n-----')
    return render(request, 'product-details.html', context={'product': product,
                                                            'visits': visits})


# def shop(request):
#     print(f'-----\n{request}\n-----')
#     return render(request, 'shop.html')


def wishlist(request):
    print(f'-----\n{request}\n-----')
    return render(request, 'wishlist.html')


class ProductListViews(generic.ListView):
    model = Product
    paginate_by = 30
    template_name = 'shop.html'
    context_object_name = 'product_list'

    def get_queryset(self):
        return Product.objects.filter(availability=True)
        # return Product.objects.all()


class ProductCategoryListViews(generic.ListView):
    model = Product
    paginate_by = 30
    template_name = 'shop.html'
    context_object_name = 'product_list'

    def get_queryset(self):
        return Product.objects.filter(category__slug=self.kwargs['category_slug'], availability=True)

