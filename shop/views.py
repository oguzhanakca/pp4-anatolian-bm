from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import Product, Cart, CartItem, Order, OrderItem

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
    # Get Product
    queryset = Product.objects.all()
    product = get_object_or_404(queryset, id=id)
    # Get or Create Shopping Cart
    cart = Cart.objects.get_or_create(user=request.user)
    # Increase Cart Product Quantity or Add it to Cart
    if request.method == "POST":
        cart_item = CartItem.objects.get_or_create(cart=cart, product=product)
        cart_item.quantity +=1
        cart_item.save()

    return render(request, "shop/product_detail.html", {"product": product})