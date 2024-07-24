from django.db import models
from django.contrib.auth.models import User

CATEGORY = ((0, "Fruit and Vegetable"), (1, "Meat"), (2, "Seafood"),(3, "Ice Cream"), (4, "Drink"), (5, "Bakery"), (6, "Dairy"))

class Product(models.Model):
    """
    Product Model
    """
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(null=True, blank=True)
    category = models.IntegerField(choices=CATEGORY)
    image = models.ImageField(upload_to="product_images/", null=False, blank=False, default="No Image")
    price = models.DecimalField(max_digits=10,decimal_places=2,default=0.0)
    stock = models.IntegerField(default=0)
    sold = models.PositiveBigIntegerField(default=0)
    on_sale = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name
    
class Cart(models.Model):
    """
    Shopping Cart Model
    """
    id = models.BigAutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='cart')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}'s Cart Id : {self.id}"

    def get_total_cost(self):
        return sum(product.get_cost() for product in self.products.all())
    
class CartItem(models.Model):
    """
    Model for the item in the shopping cart
    """
    id = models.BigAutoField(primary_key=True)
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='cart_items', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.product.name}"

    def get_cost(self):
        return self.product.price * self.quantity

class Order(models.Model):
    """
    Order Model
    """
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    def __str__(self):
        return f"Order {self.id} by {self.user.username}"
    
class OrderItem(models.Model):
    """
    Order Item Model
    """
    id = models.BigAutoField(primary_key=True)
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantity} of {self.product.name} for order {self.order.id}"

    def get_cost(self):
        return self.price * self.quantity