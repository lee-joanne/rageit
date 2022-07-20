from django import forms
from django.forms import ModelForm
from .models import Post, Comment


class PostForm(ModelForm):
    """
    Class for the form the user will interact with
    """
    class Meta:
        model = Post
        fields = ['title', 'content', 'featured_image']