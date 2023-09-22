from django.db.models import Count
from . models import Category, Basket
from django.contrib.auth.models import AnonymousUser


def header_categories(request):

    category_ids_to_display = [733, 175, 172, 476, 593, 680]
    categories = Category.objects.filter(id__in=category_ids_to_display).annotate(
        products_count=Count('products')).order_by('-products_count')

    basket_items = []
    if request.user.is_authenticated:
        basket_items = Basket.objects.filter(user=request.user)
    total_quantity = sum(item.quantity for item in basket_items)
    for item in basket_items:
        item.subtotal = item.product.price * item.quantity
    total_amount = sum(item.subtotal for item in basket_items)
    return {
        'categories': categories,
        'total_quantity': total_quantity,
        'total_amount': total_amount
    }

