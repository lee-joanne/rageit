from django import forms
from django.forms import ModelForm
from .models import Post, Comment


class PostForm(ModelForm):
    """
    Class for the post form the user will interact with
    """
    class Meta:
        model = Post
        fields = ['title', 'content', 'featured_image']


class CommentForm(ModelForm):
    """
    Class for the comment form the user will interact with
    """
    class Meta:
        model = Comment
        fields = ['content', ]