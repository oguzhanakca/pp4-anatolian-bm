from django.db import models

CATEGORY = ((0, "Fruit and Vegetable"), (1, "Meat"), (2, "Seafood"),(3, "Frozen Products"), (4, "Drink"), (5, "Bakery"), (6, "Dairy"))

class Product(models.Model):
    """
    Product Model
    """
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=200, unique=True)
    category = models.IntegerField(choices=CATEGORY)
    description = models.TextField()
    stock = models.IntegerField(default=0)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.id} : {self.name}"