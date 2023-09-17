from django.db import models

from users.models import User


class Brand(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Brand name')
    logo = models.ImageField(upload_to='images/brand', blank=True, null=True, verbose_name='Image')

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=250, verbose_name='Title')
    slug = models.SlugField(max_length=255, unique=True, verbose_name='Slug')
    price = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True, verbose_name='Price')
    old_price = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True, verbose_name='Old Price')
    article = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True, verbose_name='Product Article')
    description = models.TextField(blank=True, verbose_name='Description')
    categories = models.ManyToManyField('Category', related_name='products')
    availability = models.BooleanField(default=True)
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, related_name='products', null=True, blank=True)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ['title']

    def __str__(self):
        return self.title


class Image(models.Model):
    product = models.ForeignKey('shop.Product', on_delete=models.CASCADE, related_name='images')
    url = models.URLField(max_length=512, verbose_name='Image URL')
    image = models.ImageField(upload_to='images/product', max_length=300)

    def __str__(self):
        return self.image.url


class Category(models.Model):
    title = models.CharField(max_length=50, default='Title', verbose_name='Title')
    slug = models.SlugField(max_length=100, unique=True, verbose_name='Slug')
    image = models.ImageField(upload_to='images/category', blank=True, null=True, verbose_name='Image')

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title


class Basket(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)
