from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.http import HttpResponse
from django.conf import settings
from walkease.store.models import Category, Order, Product, OrderItem, Review
from .forms import ReviewForm

def index(request):
    return render(request, "store/index.html")

def product_list(request, slug=None):
    category = None
    products = Product.objects.all()

    if slug:
        category = get_object_or_404(Category, slug=slug)
        products = products.filter(category=category)

    return render(request, "store/productlist.html", {
        "products": products,
        "category": category,
        "all_categories": Category.objects.all(),
    })

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, "store/product_detail.html", {"product": product})



@login_required
def buy_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == "POST":
        # Handle cart submission
        if request.POST.get("add_to_cart"):
            quantity = request.POST.get("quantity", 1)
            size = request.POST.get("size", "")
            try:
                quantity = int(quantity)
                if quantity < 1:
                    raise ValidationError("Quantity must be at least 1.")
                if quantity > product.stock:
                    raise ValidationError("Not enough stock available.")
            except (ValueError, ValidationError) as e:
                return HttpResponse(str(e), status=400)

            order, _ = Order.objects.get_or_create(
                user=request.user,
                status="Cart",
                defaults={
                    "shipping_address": "",
                    "payment_method": "",
                    "total_price": 0,
                }
            )

            existing_item = order.items.filter(product=product, size=size).first()
            if existing_item:
                existing_item.quantity += quantity
                existing_item.save()
            else:
                item = OrderItem.objects.create(product=product, quantity=quantity, size=size)
                order.items.add(item)

            order.total_price = sum(
                item.product.price * item.quantity for item in order.items.all()
            )
            order.save()
            return redirect("cart:view_cart")

        # Handle review submission
        elif request.POST.get("submit_review"):
            review_form = ReviewForm(request.POST)
            if review_form.is_valid():
                review = review_form.save(commit=False)
                review.product = product
                review.user = request.user
                review.display = True  # always mark new reviews as public by default
                review.save()
                return redirect("store:buy_product", product_id=product.id)
    else:
        # Pre-fill rating=5 on new review form
        review_form = ReviewForm(initial={"rating": 5})

    return render(request, "store/buy_product.html", {
        "product":     product,
        "reviews":     product.reviews.filter(display=True),
        "review_form": review_form,
    })

def contact(request):
    if request.method == "POST":
        # You can integrate email or save to DB here
        return redirect("store:index")
    return render(request, "store/contact.html")
