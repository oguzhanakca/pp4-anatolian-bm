from django.shortcuts import render

# Create your views here.
def home(request):
    """
    Display homepage
    """

    return render(
        request,
        "home/index.html",
    )

def about(request):
    """
    Display About Us page
    """
    return render(request,"home/about.html")