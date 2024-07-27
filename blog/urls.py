from . import views
from django.urls import path

urlpatterns = [
    path("", views.posts, name="blog"),
    path('<int:id>/', views.post_detail, name='post_detail'),
    path('create_post/', views.create_post, name='create_post'),
    path('<int:id>/edit/', views.update_post, name='update_post'),
]