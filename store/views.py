from django.shortcuts import get_object_or_404, render

from category.models import Category
from .models import Product

# Create your views here.


def store(request, category_slug=None):
    if category_slug:
        selected_category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(
            category=selected_category, is_available=True)
        products_count = products.count()
    else:
        products = Product.objects.all().filter(is_available=True)
        products_count = products.count()
    context = {
        'products': products,
        'products_count': products_count,
    }
    return render(request, 'store/store.html', context)
