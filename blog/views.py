from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.core.paginator import Paginator


@login_required
def posts(request):
    """
    Display all posts
    """
    # Published posts
    all_posts = Post.objects.filter(status=1)
    search_query = request.GET.get('post-search')
    if search_query:
        posts = all_posts.filter(title__icontains=search_query)
    else:
        posts = all_posts
    paginator = Paginator(posts, 7)
    page_number = request.GET.get("page")
    paginated_posts = paginator.get_page(page_number)

    return render(
        request,
        "blog/posts.html",
        {"posts": paginated_posts,
         "query": search_query},
    )


@login_required
def create_post(request):
    """
    Display create post page
    """
    # Published posts

    form = PostForm(data=request.POST)
    if form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        post.save()
        return redirect('post_detail', id=post.id)
    else:
        form = PostForm()

    return render(
        request,
        "blog/create_post.html",
        {"form": form},
    )


@login_required
def post_detail(request, id):
    """
    Display the specified post from its id.
    """
    queryset = Post.objects.all()
    post = get_object_or_404(queryset, id=id)
    # Approved comments
    comments = Comment.objects.filter(
        post_id=post.id, approved=True).order_by("-created_at")
    # Pagination
    paginator = Paginator(comments, 15)
    page_number = request.GET.get("page")
    paginated_comments = paginator.get_page(page_number)
    # Comment Form
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            form.save()
            return redirect('post_detail', id=post.id)
    else:
        form = CommentForm()

    return render(
        request,
        "blog/post_detail.html",
        {"post": post,
         "comments": paginated_comments,
         "form": form},
    )


@login_required
def update_post(request, id):
    """
    Display update post page
    """
    post = Post.objects.get(id=id)
    if post.author != request.user:
        raise Http404("You are not allowed to edit this post")

    if request.method == 'POST':
        if 'delete' in request.POST:
            post.delete()
            return redirect('blog')
        else:
            form = PostForm(request.POST, instance=post)
            if form.is_valid():
                form.save()
                return redirect('post_detail', id=post.id)
    else:
        form = PostForm(instance=post)

    return render(request, "blog/update_post.html", {
        "post": post, "form": form})
