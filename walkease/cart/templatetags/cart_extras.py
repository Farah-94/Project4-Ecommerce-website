from django import template

register = template.Library()

@register.filter
def currency(value):
    """Format number as GBP (£12.34)"""
    return f"£{value:.2f}"

    
import os

@register.filter
def basename(value):
    """Extracts just the file name from a path"""
    return os.path.basename(value)
