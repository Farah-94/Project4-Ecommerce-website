from django import template

register = template.Library()

@register.filter
def currency(value):
    """Format number as GBP (£12.34)"""
    return f"£{value:.2f}"
