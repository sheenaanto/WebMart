from urllib import request
from django.shortcuts import redirect, render

from carts.models import Cart, CartItem
from store.models import Product

# Create your views here.


def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart


def add_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))

    except Cart.DoesNotExist:
        cart = Cart.objects.create(cart_id=_cart_id(request))
    cart.save()

    try:
        cart_item = CartItem.objects.get(product=product, cart=cart)
        cart_item.quantity += 1

    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(
            product=product, cart=cart, quantity=1)
    cart_item.save()
    return redirect('storecart')


def cart(request, total=0, quantity=0, cart_items=None):
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart, is_active=True)
    except Cart.DoesNotExist:
        pass
    context = {
        'cart_items': cart_items,
        'total': total,
        'quantity': quantity,
    }

    return render(request, 'store/carts.html', context)
