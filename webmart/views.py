from django.shortcuts import render
from store.models import Product


def home(request):
    """
    Render the home page with available products.
    This view retrieves all products from the database that are marked as 
    available and passes them to the home template for display.
    Args:
        request (HttpRequest): The HTTP request object.
    Returns:
        HttpResponse: Rendered home.html template with available products in
    context.
    """
    products = Product.objects.all().filter(is_available=True)
    context = {
        'products': products,
    }
    return render(request, 'home.html', context)
