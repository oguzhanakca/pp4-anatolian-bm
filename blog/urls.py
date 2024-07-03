from . import views
from django.urls import path

urlpatterns = [
    path("", views.posts, name="blog"),
    path('<int:id>/', views.post_detail, name='post_detail'),

]