from django.shortcuts import render


def home(request):
    """
    Display homepage
    """

    return render(
        request,
        "home/index.html",
    )
