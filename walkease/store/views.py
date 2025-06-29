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
    review_form = ReviewForm(initial={"rating": 5})
    sizes = ["6", "7", "8", "9", "10"]  # Send size options to template

    if request.method == "POST":
        # Handle Add to Cart
        if request.POST.get("add_to_cart"):
            return redirect("cart:view_cart")

        # Handle Review Submission
        elif request.POST.get("submit_review"):
            print("📝 REVIEW POST TRIGGERED on Heroku!")
            review_form = ReviewForm(request.POST)

            if review_form.is_valid():
                review = review_form.save(commit=False)
                review.product = product
                review.user = request.user
                review.display = True
                review.save()

                return redirect("store:buy_product", product_id=product.id)
            else:
                print("❌ Review form errors:", review_form.errors)

    return render(request, "store/buy_product.html", {
        "product": product,
        "reviews": product.reviews.filter(display=True),
        "review_form": review_form,
        "sizes": sizes,
    })




def contact(request):
    if request.method == "POST":
        # You can integrate email or save to DB here
        return redirect("store:index")
    return render(request, "store/contact.html")
