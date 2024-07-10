from django.db import models

CATEGORY = ((0, "Fruit and Vegetable"), (1, "Meat"), (2, "Seafood"),(3, "Frozen Products"), (4, "Drink"), (5, "Bakery"), (6, "Dairy"))

class Product(models.Model):
    """
    Product Model
    """
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(null=True, blank=True)
    category = models.IntegerField(choices=CATEGORY)
    image = models.ImageField(upload_to="product_images/")
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