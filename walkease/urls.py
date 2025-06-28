"""
URL configuration for walkease project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# walkease/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from walkease.cart.views import (
    CustomLoginView,
    CustomSignupView,
    CustomLogoutView,
)

urlpatterns = [
    path("admin/", admin.site.urls),

    # --- Your cart-styled auth endpoints in the root namespace ---
    path(
        "cart/signin/",
        CustomLoginView.as_view(),    # CBV LoginView
        name="account_login",
    ),
    path(
        "cart/signup/",
        CustomSignupView.as_view(),   # CBV SignupView
        name="account_signup",
    ),
    path(
        "cart/signout/",
        CustomLogoutView,             # function-based logout
        name="account_logout",
    ),

    # --- Now your regular cart URLs (no auth in here) ---
    path("cart/", include("walkease.cart.urls")),

    # --- All the rest of allauth’s built-ins (password reset, social, etc.) ---
    path("accounts/", include("allauth.urls")),

    # --- Other apps ---
    path("user/",     include("walkease.user.urls",    namespace="user")),
    path("",          include("walkease.store.urls",   namespace="store")),
    path("checkout/", include("walkease.checkout.urls",namespace="checkout")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)