from . import views
from django.urls import path

urlpatterns = [
    path("", views.shop, name="shop"),
    path('<int:id>/', views.product_detail, name='product_detail'),
    path('add_cart_success/', views.add_cart_success, name='add_cart_success'),
    path('all_products/', views.all_products, name='all_products'),
    path('my_cart/', views.my_cart, name='my_cart'),

]