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
    # 🎯 1. Get the product or return 404 if it doesn't exist
    product = get_object_or_404(Product, id=product_id)

    # ✍️ 2. Create a blank review form (in case we need to show it later)
    review_form = ReviewForm(initial={"rating": 5})  # Default rating shown

    # 🚦 3. If this is a POST request (form submission)
    if request.method == "POST":
        # 🛒 3a. User clicked "Add to Cart" — handled elsewhere
        if request.POST.get("add_to_cart"):
            # Your add-to-cart logic goes here...
            return redirect("cart:view_cart")

        # 📝 3b. User submitted a review
        elif request.POST.get("submit_review"):
            review_form = ReviewForm(request.POST)  # Load posted data into form

            if review_form.is_valid():
                # Save review with additional fields
                review = review_form.save(commit=False)
                review.product = product
                review.user = request.user
                review.display = True  # Mark as approved
                review.save()

                # Redirect back to the same page to show new review
                return redirect("store:buy_product", product_id=product.id)
            else:
                # Optional: log errors during development
                print("❌ Review form errors:", review_form.errors)

    # 📦 4. Load existing reviews and render the page
    return render(request, "store/buy_product.html", {
        "product": product,
        "reviews": product.reviews.filter(display=True),
        "review_form": review_form,
    })

def contact(request):
    if request.method == "POST":
        # You can integrate email or save to DB here
        return redirect("store:index")
    return render(request, "store/contact.html")
