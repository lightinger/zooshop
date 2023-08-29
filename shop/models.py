from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(unique=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    old_price = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    availability = models.BooleanField(default=True)
    article = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    description = models.TextField()
    details = models.CharField(max_length=1000)


class Image(models.Model):
    url = models.URLField()
    image = models.ImageField(upload_to='images')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='picture')

