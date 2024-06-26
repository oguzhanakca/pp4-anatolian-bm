from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    list_display = ('id','title', 'status','created_at')
    search_fields = ['title','content']
    list_filter = ('status','created_at')

# Register your models here.
admin.site.register(Comment)
