from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
from django.views import generic
from .models import Product, Category


def index(request):
    products_list = Product.objects.all()
    category_list = Category.objects.all()
    context = {
        'products_list': products_list,
        'category_list': category_list,
    }

    return render(request, 'index.html', context=context)


def home(request):
    products_list = Product.objects.all()
    category_list = Category.objects.all()
    context = {
        'products_list': products_list,
        'category_list': category_list,
    }

    return render(request, 'index.html', context=context)

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
    context = {
        'product': product,
        'visits': visits,
    }
    return render(request, 'product-details.html', context=context)


def shop(request):
    product_list = Product.objects.all()
    category_list = Category.objects.all()
    context = {
        'product_list': product_list,
        'category_list': category_list,
        'category_selected': 0,
    }
    print(f'-----\n{request}\n-----')
    return render(request, 'shop.html', context=context)


def shop_category(request, cat_id):
    product_list = Product.objects.filter(cat_id=cat_id)
    category_list = Category.objects.all()

    context = {
        'product_list': product_list,
        'category_list': category_list,
        'category_selected': cat_id,
    }
    print(f'-----\n{request}\n-----')
    return render(request, 'shop.html', context=context)


def wishlist(request):
    print(f'-----\n{request}\n-----')
    return render(request, 'wishlist.html')


# class ProductListViews(generic.ListView):
#     model = Product
#     paginate_by = 30
#     template_name = 'shop.html'
#     context_object_name = 'product_list'
#
#     def get_queryset(self):
#         return Product.objects.filter(availability=True)



# class ProductCategoryListViews(generic.ListView):
#     model = Product
#     paginate_by = 30
#     template_name = 'shop.html'
#     context_object_name = 'product_list'
#
#     def get_queryset(self):
#         return Product.objects.filter(category__slug=self.kwargs['category_slug'], availability=True)

