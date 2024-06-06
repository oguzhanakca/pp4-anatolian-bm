from django.shortcuts import render

# Create your views here.

def about(request):
    """
    Display About Us page
    """
    return render(request,"about/about.html")