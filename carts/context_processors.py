

from carts.models import Cart, CartItem
from carts.views import _cart_id


def counter(request):
    cart_count = 0
    if 'admin' in request.path:
        return {}
    else:
        try:
            # the counter runs on every page, including pages where the user has no cart yet, .get() is risky.
            cart = Cart.objects.filter(cart_id=_cart_id(request)).first()
            # cart = Cart.objects.get(cart_id=_cart_id(request))
            cart_items = CartItem.objects.filter(cart=cart)

            for cart_item in cart_items:
                cart_count += cart_item.quantity
        except Cart.DoesNotExist:
            cart_count = 0

    return dict(cart_count=cart_count)
