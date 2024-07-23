from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import Product

@login_required
def shop(request):
    """
    Display Shop homepage
    """

    products = Product.objects.filter(on_sale=True)
    most_sellers = products.order_by("-sold")[:12]
    latest_products = products.order_by("-created_at")[:12]

    return render(request, "shop/shop.html",{"products": products,"most_sellers":most_sellers,"latest_products":latest_products})

@login_required
def product_detail(request, id):
    """
    Displays Product Detail page
    """
    queryset = Product.objects.all()
    product = get_object_or_404(queryset, id=id)

    return render(request, "shop/product-detail.html", {"product": product})