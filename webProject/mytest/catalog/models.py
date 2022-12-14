from django.db import models

# Create your models here.
from django.urls import reverse


class Product(models.Model):

    name = models.CharField(max_length=100, help_text='Product name', default=None)
    price = models.FloatField(help_text='Product price', default=0)
    availability = models.BooleanField(help_text='Product availability', default=True)
    description = models.CharField(max_length=500, help_text='Product description', default=None)
    # reviews = models.CharField(max_length=500, help_text='Product reviews', default=None)
    images = models.ImageField(help_text='Product images', default=None)
    category = models.CharField(max_length=50, help_text='Product category', default=None)
    brend = models.CharField(max_length=50, help_text='Product BREND', default=None)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product-details', args=[str(self.id)])
