from . import views
from django.urls import path

urlpatterns = [
    path("book", views.book, name="book"),
    path("booking_success", views.booking_success, name="booking_success"),

]