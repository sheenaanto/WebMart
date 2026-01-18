from django.contrib import messages, auth
from django.shortcuts import redirect, render
from accounts.forms import RegistrationForm
from accounts.models import Account
from django.contrib.auth.decorators import login_required

from carts.models import Cart, CartItem
from carts.views import _cart_id
# Create your views here.


def register(request):
    if (request.method == 'POST'):
        form = RegistrationForm(request.POST)
        if form.is_valid():  # if form has all the required fields
            # fetching all the fields from the request post
            # cleaned data gives the validated value instead of raw unvalidated strings
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            password = form.cleaned_data['password']
            username = email.split('@')[0]
            user = Account.objects.create_user(
                first_name=first_name, last_name=last_name, email=email, username=username, password=password)
            user.phone_number = phone_number
            user.save()
            messages.success(
                request, "You have registered successfully")
            return redirect('login')

    else:
        form = RegistrationForm()
    context = {'form': form}
    return render(request, 'accounts/register.html', context)


def login(request):
    if (request.method == 'POST'):
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(email=email, password=password)

        if user:
            try:
                # guest cart
                cart = Cart.objects.get(cart_id=_cart_id(request))
                cart_items = CartItem.objects.filter(cart=cart)
                for item in cart_items:
                    # Check if user already has this product in cart
                    try:
                        existing_item = CartItem.objects.get(
                            product=item.product, user=user)
                        existing_item.quantity += item.quantity
                        existing_item.save()
                        item.delete()
                    except CartItem.DoesNotExist:
                        item.user = user
                        item.cart = None
                        item.save()
            except Cart.DoesNotExist:
                pass

            auth.login(request, user)
            messages.success(request, "You are now logged in.")
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid login credentials")
            return redirect('login')

    return render(request, 'accounts/login.html')


@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('login')


@login_required(login_url='login')
def dashboard(request):
    return render(request, 'accounts/dashboard.html')
