from django.shortcuts import render

# Create your views here.
def booking(request):
    """
    Display an individual :model:`blog.Post`.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.

    **Template:**

    :template:`blog/post_detail.html`
    """

    return render(
        request,
    )