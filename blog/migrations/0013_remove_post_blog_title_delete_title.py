# Generated by Django 4.2.13 on 2024-06-28 16:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_remove_title_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='blog_title',
        ),
        migrations.DeleteModel(
            name='Title',
        ),
    ]
