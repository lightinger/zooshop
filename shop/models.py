from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=250, verbose_name='Title')
    slug = models.SlugField(max_length=255, unique=True, verbose_name='Slug')
    price = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True, verbose_name='Price')
    old_price = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True, verbose_name='Old Price')
    article = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True, verbose_name='Product Article')
    description = models.TextField(blank=True, verbose_name='Description')
    categories = models.ManyToManyField('Category', related_name='products')
    availability = models.BooleanField(default=True)


    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ['title']

    def __str__(self):
        return self.title


class Image(models.Model):
    product = models.ForeignKey('shop.Product', on_delete=models.CASCADE, related_name='images')
    url = models.URLField(max_length=512, verbose_name='Image URL')
    image = models.ImageField(upload_to='images/media', max_length=300)


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

