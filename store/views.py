from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from carts.models import CartItem
from carts.views import _cart_id
from category.models import Category
from .models import Product
from django.core.paginator import Paginator
from django.db.models import Q

# Create your views here.


def store(request, category_slug=None):
    selected_category = None
    products = None
    if category_slug:
        selected_category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(
            category=selected_category, is_available=True).order_by('id')

    else:
        products = Product.objects.all().filter(is_available=True).order_by('id')

    # pagination code
    paginator = Paginator(products, 6)
    page = request.GET.get('page')
    products_count = products.count()
    paged_products = paginator.get_page(page)

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
        if request.user.is_authenticated:
            in_cart = CartItem.objects.filter(
                user=request.user, product=single_product).exists()
        else:
            in_cart = CartItem.objects.filter(
                cart__cart_id=_cart_id(request), product=single_product).exists()

    except Exception as e:
        raise e

    context = {
        'single_product': single_product,
        'in_cart': in_cart,
    }

    return render(request, 'store/product_detail.html', context)


def search(request):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            # Q()-combine multiple conditions using OR (|) or AND (&)
            products = Product.objects.filter(
                Q(description__icontains=keyword) | Q(product_name__icontains=keyword))
            products_count = products.count()
            context = {
                'products': products,
                'products_count': products_count,
            }
            return render(request, 'store/store.html', context)
        else:
            return render(request, 'store/store.html')
