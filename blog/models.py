from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Hidden"), (1, "Published"))
CATEGORY = ((0, "Restaurant"), (1, "Market"), (2, "General"))

class Title(models.Model):
    """
    The model of main titles
    """
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    image =  models.ImageField(upload_to="images/")
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

class Post(models.Model):
    """
    The user post model
    """
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts")
    blog_title = models.ForeignKey(Title, on_delete=models.CASCADE, related_name="blog_post_title")
    category = models.IntegerField(choices=CATEGORY)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=1)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.title} : {self.author}"
    

class Comment(models.Model):
    """
    The user comment model
    """
    id = models.BigAutoField(primary_key=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField()
    approved = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.body} : {self.author}"
