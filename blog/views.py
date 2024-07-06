from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from .forms import CommentForm
from django.core.paginator import Paginator

# Create your views here.
@login_required
def posts(request):
    """
    Display posts
    """
    # Published posts
    posts = Post.objects.filter(status=1)
    paginator = Paginator(posts, 15)
    page_number = request.GET.get("page")
    paginated_posts = paginator.get_page(page_number)

    return render(
        request, 
        "blog/posts.html", 
        {"posts": paginated_posts},
    )

@login_required
def post_detail(request, id):
    """
    Display the post.
    """
    queryset = Post.objects.all()
    post = get_object_or_404(queryset, id=id)
    # Approved comments
    comments = Comment.objects.filter(post_id=post.id, approved=True).order_by("-created_at")
    paginator = Paginator(comments, 15)
    page_number = request.GET.get("page")
    paginated_comments = paginator.get_page(page_number)
    if request.method == 'POST':
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.author = request.user
                comment.post = post
                comment.save()
                form.save()
                return redirect('post_detail', id=post.id)  # Adjust the redirect as needed
    else:
        form = CommentForm()

    return render(
        request,
        "blog/post_detail.html",
        {"post": post,
         "comments":paginated_comments,
         "form":form},
    )
