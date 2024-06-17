from . import views
from django.urls import path

urlpatterns = [
    path("", views.book, name="booking"),
    path("booking_success", views.booking_success, name="booking_success"),

]