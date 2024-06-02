from . import views
from django.urls import path

urlpatterns = [
    path("posts/", views.PostList.as_view(), name="blog-home"),
]