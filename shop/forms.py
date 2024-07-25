from django import forms
from .models import Product

class OrderAndFilterForm(forms.Form):
    """
    Order and Filter Options for Products
    """
    FILTER_OPTIONS = [("all", 'All')] + list(Product.CATEGORY)
    ORDER_OPTIONS = [
        ('name', 'Name (Ascending)'),
        ('-name', 'Name (Descending)'),
        ('sold', 'Least Sold'),
        ('-sold', 'Most Sold'),
    ]
    order_options = forms.ChoiceField(choices=ORDER_OPTIONS)
    filter_options = forms.ChoiceField(choices=FILTER_OPTIONS)
