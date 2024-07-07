from django.shortcuts import render

def shop(request):
    """
    Display Shop homepage
    """

    return render(request,"shop/shop.html")
