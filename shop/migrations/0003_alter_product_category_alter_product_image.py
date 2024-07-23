# Generated by Django 4.2.13 on 2024-07-14 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_alter_product_sold'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.IntegerField(choices=[(0, 'Fruit and Vegetable'), (1, 'Meat'), (2, 'Seafood'), (3, 'Ice Cream'), (4, 'Drink'), (5, 'Bakery'), (6, 'Dairy')]),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='No Image', upload_to='product_images/'),
        ),
    ]