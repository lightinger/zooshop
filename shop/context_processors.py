from django.db.models import Count
from django.shortcuts import HttpResponseRedirect

from . models import Category, Product, Basket


def header_categories(request):
    categories = Category.objects.annotate(products_count=Count('products')).order_by('-products_count')[1:7]
    category_ids_to_display = [54, 175, 172, 476, 593, 680]  # Замените этот список нужными вам ID категорий
    categories = Category.objects.filter(id__in=category_ids_to_display).annotate(
        products_count=Count('products')).order_by('-products_count')
    return {
        'categories': categories
    }

