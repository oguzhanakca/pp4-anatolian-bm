from . import views
from django.urls import path

urlpatterns = [
    path("", views.shop, name="shop"),
    path('<int:id>/', views.product_detail, name='product_detail'),
    path('add_cart_success/', views.add_cart_success, name='add_cart_success'),
    path('all_products/', views.all_products, name='all_products'),
    path('shopping_cart/', views.all_products, name='shopping_cart'),

]