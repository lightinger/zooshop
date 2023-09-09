from django.contrib import admin
from django.urls import path
from .views import index, catalog, about, contact, faq, product

urlpatterns = [
    path('', index, name='index'),
    path('catalog/<slug:slug>', catalog, name='catalog'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('faq/', faq, name='faq'),
    path('product/<slug:slug>', product, name='product'),
]
