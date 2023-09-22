from django.contrib import admin
from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name='index'),
    path('catalog/<slug:slug>', views.catalog, name='catalog'),
    path('catalog/<slug:slug>/', views.catalog, name='catalog_sorted'),
    path('about/', views.about, name='about'),
    path('contact-us/', views.ContactUsView.as_view(), name='contact'),
    path('faq/', views.faq, name='faq'),
    path('product/<slug:slug>/', views.product, name='product'),
    path('blog/', views.blog, name='blog'),
    path('blog-details/', views.blog_details, name='blog-details'),
    path('basket/add/<int:product_id>/', views.basket_add, name='basket_add'),
    path('basket/remove/<int:product_id>/', views.basket_remove, name='basket_remove'),
    path('basket/', views.basket_view, name='basket'),
    path('login-register/', views.LoginRegisterView.as_view(), name='login-register'),
    path('checkout/', views.checkout, name='checkout'),
    path('search/', views.search_product, name='search'),
]
