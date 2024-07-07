from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

@login_required
def shop(request):
    """
    Display Shop homepage
    """

    return render(request,"shop/shop.html")
