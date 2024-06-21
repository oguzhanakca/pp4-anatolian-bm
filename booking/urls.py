from . import views
from django.urls import path

urlpatterns = [
    path("book", views.book, name="book"),
    path("booking-success", views.booking_success, name="booking_success"),
    path("booking-list", views.booking_list, name="booking_list")
]