from django import forms
from .models import Product, CartItem


class OrderAndFilterForm(forms.Form):
    """
    Order and Filter Options for Products
    """
    FILTER_OPTIONS = [("99", 'All')] + list(Product.CATEGORY)
    ORDER_OPTIONS = [
        ('name', 'Name (Ascending)'),
        ('-name', 'Name (Descending)'),
        ('sold', 'Least Sold'),
        ('-sold', 'Most Sold'),
    ]
    order_options = forms.ChoiceField(choices=ORDER_OPTIONS)
    filter_options = forms.ChoiceField(choices=FILTER_OPTIONS)
    search = forms.CharField(required=False, max_length=100)
