from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import Product

@login_required
def shop(request):
    """
    Display Shop homepage
    """

    products = Product.objects.filter(on_sale=True)
    most_sellers = products.order_by("-sold")[:6]
    latest_products = products.order_by("-created_at")[:6]

    return render(request,"shop/shop.html",{"products": products,"most_sellers":most_sellers,"latest_products":latest_products})
