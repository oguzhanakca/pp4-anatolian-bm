from django.contrib import admin
from .models import Post, Comment, Title
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    list_display = ('id','title', 'status','created_at')
    search_fields = ['title','content']
    list_filter = ('status','created_at','blog_title__name')

# Register your models here.
admin.site.register(Comment)
admin.site.register(Title)
