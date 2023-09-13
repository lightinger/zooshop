from django.contrib import admin
from django.urls import path
from .views import index, catalog, about, contact, faq, product, blog, blog_details, cart, login_register, checkout

urlpatterns = [
    path('', index, name='index'),
    path('catalog/<slug:slug>', catalog, name='catalog'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('faq/', faq, name='faq'),
    path('product/<slug:slug>', product, name='product'),
    path('blog/', blog, name='blog'),
    path('blog-details/', blog_details, name='blog-details'),
    path('cart/', cart, name='cart'),
    path('login-register/', login_register, name='login-register'),
    path('checkout/', checkout, name='checkout'),
]
