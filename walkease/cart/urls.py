from django.urls import path
from allauth.account import views as a_views
from . import views
from allauth.account.views import LoginView

path("signin/", LoginView.as_view(), name="account_login"),

app_name = "cart"

urlpatterns = [
    path("view/", views.cart_view, name="view_cart"),
    path("add/<int:product_id>/", views.add_to_cart, name="add_to_cart"),
    path("update/<int:item_id>/<str:action>/", views.update_cart, name="update_cart"),
    path("remove/<int:item_id>/", views.remove_from_cart, name="remove_from_cart"),

    # Allauth views using default template discovery
    path("signup/", a_views.SignupView.as_view(), name="account_signup"),
    path("signin/", a_views.LoginView.as_view(), name="account_login"),

    path("signout/", a_views.LogoutView.as_view(), name="account_logout"),
]
