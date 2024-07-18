from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'status','created_at','author')
    search_fields = ['title','author__username']
    list_filter = ('status','created_at')

# Register your models here.
admin.site.register(Comment)
