from django.db import models

# Create your models here.
from django.urls import reverse


class Product(models.Model):

    name = models.CharField(max_length=100, help_text='Product name', default=None)
    slug = models.SlugField(max_length=100, help_text='URL', unique=True, db_index=True)
    price = models.FloatField(help_text='Product price', default=0)
    availability = models.BooleanField(help_text='Product availability', default=True)
    description = models.CharField(max_length=500, help_text='Product description', default=None)
    # reviews = models.CharField(max_length=500, help_text='Product reviews', default=None)
    images = models.ImageField(help_text='Product images', default=None)
    category = models.CharField(max_length=50, help_text='Product category', default=None)
    brend = models.CharField(max_length=50, help_text='Product BREND', default=None)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        s = self.slug.replace('/','').replace(')','').replace('(','').replace('#','').replace('\'','')\
            .replace('’','').replace('?','')
        return reverse('product-details', kwargs={'prod_slug': s})

    class Meta:
        verbose_name = 'Коллекционные игрушки FUNKO'
        verbose_name_plural = 'Коллекционные игрушки FUNKO'
        ordering = ['name', 'cat']


class Category(models.Model):

    name = models.CharField(max_length=100, help_text='Category name', db_index=True)
    slug = models.SlugField(max_length=100, help_text='URL', unique=True, db_index=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['id', 'name',]
