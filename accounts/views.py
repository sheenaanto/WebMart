from django.contrib import messages, auth
from django.shortcuts import redirect, render
from accounts.forms import RegistrationForm
from accounts.models import Account
from django.contrib.auth.decorators import login_required

from carts.models import Cart, CartItem
from carts.views import _cart_id
from orders.models import Order
# Create your views here.


def register(request):
    """
    Handle user registration requests.
    This view processes both GET and POST requests for user registration.
    On GET requests, it displays an empty registration form.
    On POST requests, it validates the submitted form data, creates a new user 
    account with the provided information, and redirects to the login page upon
    success.
    Args:
        request (HttpRequest): The HTTP request object containing method and 
        POST data.
    Returns:
        HttpResponse: Rendered registration form template on GET request or 
        form validation failure,or redirect to login page on successful 
        registration.
    Raises:
        None
    Side Effects:
        - Creates a new Account object in the database on successful form 
        validation
        - Displays a success message to the user on successful registration
    """

    if (request.method == 'POST'):
        form = RegistrationForm(request.POST)
        if form.is_valid():  # if form has all the required fields
            # fetching all the fields from the request post
            # cleaned data gives the validated value instead of raw
            # unvalidated strings
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            password = form.cleaned_data['password']
            username = email.split('@')[0]
            user = Account.objects.create_user(
                first_name=first_name, last_name=last_name, email=email,
                username=username, password=password)
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
    """
    Handles user login functionality.
    This view function processes login requests. If the request method is 
    POST, it attempts to authenticate the user using the provided email 
    and password. If authentication is successful, it checks for an existing
    guest cart and merges its items with the user's cart. If the user is 
    successfully logged in, a success message is displayed, and the user 
    is redirected to the home page. If authentication fails, an error 
    message is shown, and the user is redirected back to the login page.
    Args:
        request: The HTTP request object containing user input.
    Returns:
        HttpResponse: A redirect to the home page upon successful login or 
            a render of the login page with error messages upon failure.
    """

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
            return redirect('home')
        else:
            messages.error(request, "Invalid login credentials")
            return redirect('login')

    return render(request, 'accounts/login.html')


@login_required(login_url='login')
def logout(request):
    """
    Logs out the user and redirects them to the login page.

    This function handles the logout process by calling the 
    authentication logout method and displaying a success message 
    to the user. After logging out, the user is redirected to 
    the login page.

    Parameters:
        request: The HTTP request object containing metadata about 
                 the request.

    Returns:
        HttpResponseRedirect: A redirect to the login page after 
                              successful logout.
    """

    auth.logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('login')


@login_required(login_url='login')
def dashboard(request):
    """
    Display user dashboard with their order history.
    Args:
        request: HttpRequest object containing user information.
    Returns:
        HttpResponse: Rendered dashboard template with user's orders and order count.
    Context:
        - orders: QuerySet of Order objects filtered by current user, ordered by creation date (newest first), only including completed orders.
        - order_count: Integer count of user's total orders.
    """

    orders = Order.objects.order_by('-created_on').filter(
        user_id=request.user.id, is_ordered=True)
    order_count = orders.count()

    context = {
        'orders': orders,
        'order_count': order_count,
    }
    return render(request, 'accounts/dashboard.html', context)
