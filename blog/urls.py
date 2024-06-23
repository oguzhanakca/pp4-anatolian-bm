from . import views
from django.urls import path

urlpatterns = [
    path("", views.title, name="blog"),
    path("discounts", views.discount, name="discounts"),
    path("events", views.event, name="events"),
    path("feedbacks", views.feedback, name="feedbacks"),

]