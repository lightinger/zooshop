from django.db.models import Count

from . models import Category


def header_categories(request):
    categories = Category.objects.all()[:10]
    return {
        'categories': categories
    }
