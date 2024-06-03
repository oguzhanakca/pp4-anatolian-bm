from . import views
from django.urls import path

urlpatterns = [
    path("", views.PostList.as_view(), name="blog_home"),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    
]