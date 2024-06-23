# Generated by Django 4.2.13 on 2024-06-23 10:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='blog_title',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='blog_title_post', to='blog.title'),
            preserve_default=False,
        ),
    ]
