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

