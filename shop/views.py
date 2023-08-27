from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def catalog(request):
    return render(request, 'shop-left-sidebar.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def faq(request):
    return render(request, 'faq.html')


def product(request):
    return render(request, 'product-details.html')
