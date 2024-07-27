from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import Product, Cart, CartItem
from .forms import OrderAndFilterForm


@login_required
def shop(request):
    """
    Display Shop homepage
    """

    products = Product.objects.filter(on_sale=True)
    most_sellers = products.order_by("-sold")[:12]
    latest_products = products.order_by("-created_at")[:12]

    return render(
        request,
        "shop/shop.html",
        {
            "products": products,
            "most_sellers": most_sellers,
            "latest_products": latest_products})


@login_required
def product_detail(request, id):
    """
    Displays Product Detail page
    """
    # Get Product
    queryset = Product.objects.all()
    product = get_object_or_404(queryset, id=id)
    related_products = queryset.filter(
        category=product.category).exclude(id=product.id)[:5]

    if request.method == "POST":
        # Get or Create Shopping Cart
        cart, created = Cart.objects.get_or_create(user=request.user)
        # Increase Cart Product Quantity or Add it to Cart
        cart_item, created = CartItem.objects.get_or_create(
            cart=cart, product=product)
        if not created:
            cart_item.quantity += 1
        else:
            cart_item.quantity = 1
        cart_item.save()

        return redirect("add_cart_success")

    return render(
        request,
        "shop/product_detail.html",
        {"product": product, "related_products": related_products})


@login_required
def add_cart_success(request):
    """
    Displays when a product successfully added to cart
    """

    return render(request, "shop/add_cart_success.html")


@login_required
def all_products(request):
    """
    Displays all products
    """

    form = OrderAndFilterForm(request.GET or None)
    all_products = Product.objects.filter(on_sale=True)

    if form.is_valid():
        order = form.cleaned_data["order_options"]
        filter = form.cleaned_data["filter_options"]
        search = form.cleaned_data["search"]

        if filter and filter != "99":
            all_products = all_products.filter(category=filter)
        if search:
            all_products = all_products.filter(name__icontains=search)
        all_products = all_products.order_by(order)

    paginator = Paginator(all_products, 10)
    page_number = request.GET.get("page")
    paginated_list = paginator.get_page(page_number)

    return render(
        request,
        "shop/all_products.html",
        {"all_products": paginated_list, "form": form})


@login_required
def my_cart(request):
    """
    Displays users shopping cart
    """
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)
    if request.method == "POST":
        for item in cart.items.all():
            quantity_str = request.POST.get(f"quantity_{item.id}")
            if quantity_str is not None:
                try:
                    quantity = int(quantity_str)
                    if quantity > 0:
                        item.quantity = quantity
                        item.save()
                    else:
                        item.delete()
                except ValueError:
                    pass
        return redirect('my_cart')
    return render(
        request,
        "shop/my_cart.html",
        {"cart": cart, "cart_items": cart_items})
