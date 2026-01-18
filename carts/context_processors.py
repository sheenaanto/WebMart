

from carts.models import Cart, CartItem
from carts.views import _cart_id


def counter(request):
    cart_count = 0

    if 'admin' in request.path:
        return {}

    session_cart_id = _cart_id(request)

    # No session cart → no items
    if not session_cart_id:
        return {'cart_count': 0}

    # Authenticated user → count user cart items only
    if request.user.is_authenticated:
        cart_items = CartItem.objects.filter(user=request.user, is_active=True)

    # Guest user → count session cart items only
    else:
        cart = Cart.objects.filter(cart_id=session_cart_id).first()

        # If no cart exists for this session, return zero
        if not cart:
            return {'cart_count': 0}

        cart_items = CartItem.objects.filter(cart=cart, is_active=True)

    # Sum quantities
    for item in cart_items:
        cart_count += item.quantity

    return {'cart_count': cart_count}


# def counter(request):
#     cart_count = 0
#     if 'admin' in request.path:
#         return {}
#     else:
#         try:
#             # the counter runs on every page, including pages where the user has no cart yet, .get() is risky.
#             cart = Cart.objects.filter(cart_id=_cart_id(request)).first()
#             if request.user.is_authenticated:
#                 cart_items = CartItem.objects.filter(user=request.user)
#             else:
#                 # cart = Cart.objects.get(cart_id=_cart_id(request))
#                 cart_items = CartItem.objects.filter(cart=cart)

#             for cart_item in cart_items:
#                 cart_count += cart_item.quantity
#         except Cart.DoesNotExist:
#             cart_count = 0

#     return dict(cart_count=cart_count)
