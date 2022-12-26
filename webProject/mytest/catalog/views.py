from django.shortcuts import render


# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from .forms import RegisterUserForm
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


def checkout(request):
    print(f'-----\n{request}\n-----')
    return render(request, 'checkout.html')


def contact(request):
    print(f'-----\n{request}\n-----')
    return render(request, 'contact.html')


class ProductDetail(DetailView):
    model = Product
    template_name = 'product-details.html'
    slug_url_kwarg = 'prod_slug'
    context_object_name = 'product'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class Shop(ListView):
    model = Product
    paginate_by = 25
    template_name = 'shop.html'
    context_object_name = 'product_list'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category_selected'] = 0
        return context

    def get_queryset(self):
        return Product.objects.filter(availability=True)


class ShopCategory(ListView):
    model = Product
    paginate_by = 25
    template_name = 'shop.html'
    context_object_name = 'product_list'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category_selected'] = context['product_list'][0].cat_id
        return context

    def get_queryset(self):
        return Product.objects.filter(cat__slug=self.kwargs['cat_slug'], availability=True)


def wishlist(request):
    print(f'-----\n{request}\n-----')
    return render(request, 'wishlist.html')


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'registration/login.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
