from datetime import date
from django.shortcuts import redirect, render

from carts.models import CartItem
from orders.models import Order, OrderProduct
from store.models import Product
from .forms import OrderForm


# Create your views here.


def place_order(request, total=0, quantity=0):
    current_user = request.user
    #  if the cart count is equal to 0, then redirect back to shop
    cart_items = CartItem.objects.filter(user=current_user)
    cart_count = cart_items.count()
    if cart_count <= 0:
        return redirect('store')
    grand_total = 0
    tax = 0
    for cart_item in cart_items:
        total += (cart_item.product.price * cart_item.quantity)
        quantity += cart_item.quantity
    tax = (2 * total)/100
    grand_total = total + tax

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if (form.is_valid()):
            data = Order()
            data.user = current_user
            data.first_name = form.cleaned_data['first_name']
            data.last_name = form.cleaned_data['last_name']
            data.phone = form.cleaned_data['phone']
            data.email = form.cleaned_data['email']
            data.address_line_1 = form.cleaned_data['address_line_1']
            data.address_line_2 = form.cleaned_data['address_line_2']
            data.country = form.cleaned_data['country']
            data.state = form.cleaned_data['state']
            data.city = form.cleaned_data['city']
            data.order_note = form.cleaned_data['order_note']
            data.order_total = grand_total
            data.tax = tax
            data.ip = request.META.get('REMOTE_ADDR')
            data.is_ordered = True
            data.save()

            # generating the order number
            today = date.today()
            current_date = today.strftime('%Y%m%d')
            order_number = current_date + str(data.id)
            data.order_number = order_number
            data.save()

            # Move the cart items to order table
            cart_items = CartItem.objects.filter(user=current_user)
            for item in cart_items:
                order_product = OrderProduct()
                order_product.order_id = data.id
                order_product.payment = None
                order_product.user_id = current_user.id
                order_product.product_id = item.product_id
                order_product.quantity = item.quantity
                order_product.product_price = item.product.price
                order_product.ordered = True
                order_product.save()

            # Reduce the quantity of the sold products
                product = Product.objects.get(id=item.product_id)
                product.stock -= item.quantity
                product.save()

            # Make a copy BEFORE deleting
            cart_items_copy = list(cart_items)
            # Clear the cart
            CartItem.objects.filter(user=current_user).delete()
            context = {
                'order_number': order_number,
                'order_placed': True,
                'cart_items': cart_items_copy,
                'total': total,
                'tax': tax,
                'grand_total': grand_total,
            }

            return render(request, 'store/checkout.html', context)

    else:
        return redirect('checkout')
