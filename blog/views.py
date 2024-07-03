from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .models import Post, Comment

# Create your views here.
@login_required
def posts(request):
    """
    Display posts
    """
    # Published posts
    posts = Post.objects.filter(status=1)

    return render(
        request, 
        "blog/posts.html", 
        {"posts": posts},
    )

@login_required
def post_detail(request, id):
    """
    Display the post.
    """

    queryset = Post.objects.all()
    post = get_object_or_404(queryset, id=id)
    # Approved comments
    comments = Comment.objects.filter(post_id=post.id, approved=True).order_by("created_at")

    return render(
        request,
        "blog/post_detail.html",
        {"post": post,
         "comments":comments},
    )
