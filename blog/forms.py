from django import forms
from .models import Post, Comment
from django_summernote.widgets import SummernoteWidget

class PostForm(forms.ModelForm):
    """
    The form for creating a post.
    """
    class Meta:
        model = Post
        fields = ['title', 'category','content']
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'content': SummernoteWidget(),
        }


class CommentForm(forms.ModelForm):
    """
    The form for commenting on a post.
    """
    class Meta:
        model = Comment
        fields = ['body']
        widgets = {
            'body': forms.Textarea(attrs={'class':'form-control', 'rows': 3, 'placeholder': 'Enter your comment'}),
        }
