from django.contrib import admin

# Register your models here.
from .models import *


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'availability', 'description', 'images', 'brend', 'cat',)
    list_display_links = ('name', 'price',)
    search_fields = ('name', 'price', 'description', 'brend', 'cat',)
    list_editable = ('availability',)
    list_filter = ('brend', 'cat', 'availability',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_display_links = ('id', 'name',)
    search_fields = ('name',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
