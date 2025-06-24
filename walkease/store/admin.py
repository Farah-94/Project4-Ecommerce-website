# walkease/store/admin.py

import os
from django import forms
from django.contrib import admin
from django.utils.html import format_html
from django.templatetags.static import static
from django.conf import settings

from .models import Product, ProductImage, Review

from django.contrib.auth.models import User, Group

# Remove Users and Groups from the admin panel
admin.site.unregister(User)
admin.site.unregister(Group)



# ------------------------------------------------------------------------------
# 1) Inline for the extra gallery images
# ------------------------------------------------------------------------------
class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1
    fields = ("filename", "preview")
    readonly_fields = ("preview",)

    def preview(self, obj):
        if obj.filename:
            name = os.path.basename(obj.filename)
            url  = static(f"store/gallery/{name}")
            return format_html(
                '<img src="{}" style="max-height:100px; '
                'object-fit:contain; border:1px solid #ccc;" />',
                url
            )
        return "(No image)"
    preview.short_description = "Preview"


# ------------------------------------------------------------------------------
# 2) Custom form for Product so the main 'image' CharField is a dropdown
# ------------------------------------------------------------------------------
class ProductAdminForm(forms.ModelForm):
    image = forms.ChoiceField(
        choices=[],
        required=False,
        label="Primary image filename"
    )
    new_category = forms.CharField(
        required=False,
        label="New Category (optional)",
        help_text="Enter a new category name if it’s not listed."
    )

    class Meta:
        model = Product
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        gallery_dir = os.path.join(
            settings.BASE_DIR,
            "walkease", "store", "static", "store", "gallery"
        )
        choices = [("", "---------")]
        if os.path.isdir(gallery_dir):
            for fname in sorted(os.listdir(gallery_dir)):
                if fname.lower().endswith(('.jpg', '.jpeg', '.png', '.gif')):
                    choices.append((fname, fname))
        self.fields["image"].choices = choices

    def clean(self):
        cleaned_data = super().clean()
        new_cat_name = cleaned_data.get("new_category")

        if new_cat_name:
            from .models import Category
            category, _ = Category.objects.get_or_create(name=new_cat_name)
            cleaned_data["category"] = category

        return cleaned_data


# ------------------------------------------------------------------------------
# 3) ProductAdmin: uses custom form + inline gallery
# ------------------------------------------------------------------------------
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    form         = ProductAdminForm
    list_display = ("name", "price", "stock")
    list_editable= ("price", "stock")
    search_fields= ("name", "description")
    list_filter  = ( "price", "stock")

    inlines = [ProductImageInline]


# ------------------------------------------------------------------------------
# 4) ReviewAdmin
# ------------------------------------------------------------------------------
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display  = ("product", "user", "rating", "created_at")
    list_filter   = ("rating", "created_at")
    search_fields = ("comment", "user__username", "product__name")

