from django.shortcuts import get_object_or_404, render

from category.models import Category
from .models import Product
from django.core.paginator import Paginator

# Create your views here.


def store(request, category_slug=None):
    if category_slug:
        selected_category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(
            category=selected_category, is_available=True)
        # pagination code
        products = Product.objects.all().filter(is_available=True)
        paginator = Paginator(products, 6)
        page = request.GET.get('page')
        products_count = products.count()
    else:
        products = Product.objects.all().filter(is_available=True)
        # pagination code
        paginator = Paginator(products, 6)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)

        products_count = products.count()
    context = {
        'products': paged_products,
        'products_count': products_count,
    }
    return render(request, 'store/store.html', context)


def product_detail(request, category_slug, product_slug):
    try:
        # Look inside the related Category object and match its slug.
        single_product = Product.objects.get(
            category__slug=category_slug, slug=product_slug)
    except Exception as e:
        raise e

    context = {
        'single_product': single_product
    }

    return render(request, 'store/product_detail.html', context)
