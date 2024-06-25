from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.db.models import OuterRef, Subquery, DateTimeField
from django.db.models.functions import Coalesce
from .models import Post, Comment, Title

# Create your views here.

@login_required
def title(request):
    """
    Display the blog homepage
    """
    titles = Title.objects.all()

    return render(
        request,
        "blog/titles.html",
        {"titles": titles},
    )

@login_required
def discount(request):
    """
    Display the discounts page
    """
    discounts_title = Title.objects.get(name="Discounts")
    discount_posts = Post.objects.filter(blog_title=discounts_title)
    latest_comment = Comment.objects.filter(post=OuterRef('pk')).order_by("-created_at")
    posts_with_latests_comment = discount_posts.annotate(latest_comment_date=Coalesce(Subquery(latest_comment.values("created_at")[:1]), None, output_field=DateTimeField()))
    ordered_posts = posts_with_latests_comment.order_by("-latest_comment_date","-created_at")
    return render(request,"blog/discounts.html",{'ordered_posts': ordered_posts})


def event(request):
    """
    Display the events page
    """
def feedback(request):
    """
    Display the feedbacks page
    """


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
