# Generated by Django 4.2.13 on 2024-06-23 16:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_post_blog_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='blog_title',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_post_title', to='blog.title'),
        ),
    ]
