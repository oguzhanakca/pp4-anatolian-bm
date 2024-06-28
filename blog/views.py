from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .models import Post, Comment

# Create your views here.

def posts(request):
    """
    Display posts
    """

@login_required
def post_detail(request, id):
    """
    Display an individual :model:`blog.Post`.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.

    **Template:**

    :template:`blog/post_detail.html`
    """

    queryset = Post.objects.all()
    post = get_object_or_404(queryset, id=id)
    comments = Comment.objects.filter(post_id=post.id).order_by("created_at")

    return render(
        request,
        "blog/post_detail.html",
        {"post": post,
         "comments":comments},
    )
