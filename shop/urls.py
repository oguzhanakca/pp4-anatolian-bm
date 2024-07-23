from . import views
from django.urls import path

urlpatterns = [
    path("", views.shop, name="shop"),
    path('<int:id>/', views.product_detail, name='product_detail'),

]