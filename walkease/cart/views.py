# walkease/cart/views.py

from django.contrib import messages
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from walkease.store.models import Product
from walkease.cart.models import CartItem

# Import Allauth’s base views
from allauth.account.views import LoginView, LogoutView


# -------------------------------
# Cart-related views
# -------------------------------

@login_required
def cart_view(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    for item in cart_items:
        item.total_price = item.product.price * item.quantity

    return render(request, "cart/cart.html", {
        "cart_items": cart_items,
        "total_price": total_price,
    })


@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    size_value = request.POST.get("size", "M")
    try:
        qty = int(request.POST.get("quantity", 1))
    except ValueError:
        qty = 1

    cart_item, created = CartItem.objects.get_or_create(
        user=request.user,
        product=product,
        size=size_value,
        defaults={"quantity": qty},
    )
    if not created:
        cart_item.quantity += qty
        cart_item.save()

    messages.success(request, f"{product.name} added to your cart!")
    return redirect("cart:view_cart")


@login_required
def update_cart(request, item_id, action):
    cart_item = get_object_or_404(CartItem, id=item_id, user=request.user)

    if action == "increase":
        cart_item.quantity += 1
        cart_item.save()
        messages.success(request, f"Increased quantity for {cart_item.product.name}.")
    elif action == "decrease":
        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.save()
            messages.success(request, f"Decreased quantity for {cart_item.product.name}.")
        else:
            cart_item.delete()
            messages.success(request, f"Removed {cart_item.product.name} from your cart.")
    else:
        messages.error(request, "Invalid action.")

    return redirect("cart:view_cart")


@login_required
def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id, user=request.user)
    cart_item.delete()
    messages.success(request, f"{cart_item.product.name} removed from your cart.")
    return redirect("cart:view_cart")



from django.contrib.auth import logout as django_logout
from django.shortcuts import render, redirect
from django.urls import reverse
from allauth.account.views import SignupView as AllauthSignupView, LoginView as AllauthLoginView
from django.http import HttpResponseRedirect
from django.contrib.sessions.models import Session
from django.contrib import messages

# … your other cart views (cart_view, add_to_cart, etc.) go above …

class CustomSignupView(AllauthSignupView):
    template_name = "account/signup.html"
    redirect_authenticated_user = True

    def form_valid(self, form):
        user = form.save(self.request)
        messages.success(self.request, "Account created! Please sign in below.")
        return redirect("account_login")  # Send them to the login page after signup

class CustomLoginView(AllauthLoginView):
    template_name = "account/login.html"
    redirect_authenticated_user = False

    def dispatch(self, request, *args, **kwargs):
        print("🎯 Reached login view")
        print("👤 Authenticated?", request.user.is_authenticated)
        print("Session keys:", request.session.keys())
        if request.user.is_authenticated:
            print("Redirecting authenticated user to store:index")
            return redirect("store:index")
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse("store:index")

def CustomLogoutView(request):
    print("🔒 CustomLogoutView hit at:", request.path)
    # Log out the user using Django's logout
    django_logout(request)
    # Flush the session to clear all data
    request.session.flush()
    # Ensure all allauth-related session keys are cleared
    for key in list(request.session.keys()):
        if key.startswith('account_'):
            del request.session[key]
    # Redirect to the login page (instead of rendering logout.html)
    messages.success(request, "You have been successfully logged out.")
    response = redirect("account_login")
    # Delete session and CSRF cookies
    response.delete_cookie("sessionid", path="/")
    response.delete_cookie("csrftoken", path="/")
    return response