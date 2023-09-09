from django.shortcuts import render, get_object_or_404
from . models import Category, Product


def index(request):
    context = {}
    return render(request, 'index.html', context=context)


def catalog(request, **kwargs):
    category = get_object_or_404(Category, slug=kwargs.get('slug'))
    products = Product.objects.filter(categories=category)[:12]
    context = {
        'products': products
    }
    return render(request, 'shop-left-sidebar.html', context=context)


def about(request):
    context = {}
    return render(request, 'about.html', context=context)


def contact(request):
    context = {}
    return render(request, 'contact.html', context=context)


def faq(request):
    context = {}
    return render(request, 'faq.html', context=context)


def product(request, **kwargs):
    single_product = get_object_or_404(Product, slug=kwargs.get('slug'))
    context = {
        'product': single_product
    }
    return render(request, 'product-details.html', context=context)
