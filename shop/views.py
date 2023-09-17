from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from . models import Category, Product, Basket
from users.models import User



def index(request):
    products = Product.objects.all()[:12]
    categories = Category.objects.all()[:6]
    context = {
        'products': products,
        'catalog': categories
    }
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
        'product': single_product,
    }

    return render(request, 'product-details.html', context=context)


def blog(request):
    context = {}
    return render(request, 'blog.html', context=context)


def blog_details(request):
    context = {}
    return render(request, 'blog-details.html', context=context)


def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)

    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


# def basket_view(request):
#     basket_items = Basket.objects.all()
#     context = {'basket_items': basket_items}
#     return render(request, 'basket.html', context)

def basket_view(request):
    basket_items = Basket.objects.all()  # Получение всех товаров в корзине
    total_quantity = sum(item.quantity for item in basket_items)
    for item in basket_items:
        item.subtotal = item.product.price * item.quantity
    total_amount = sum(item.subtotal for item in basket_items)
    context = {'basket_items': basket_items, 'total_quantity': total_quantity, 'total_amount': total_amount}
    return render(request, 'basket.html', context)


def login_register(request):
    context = {}
    return render(request, 'login-register.html', context=context)


def checkout(request):
    context = {}
    return render(request, 'checkout.html', context=context)
