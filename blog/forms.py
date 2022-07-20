from django import forms
from django.forms import ModelForm
from .models import Post, Comment
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class PostForm(ModelForm):
    """
    Class for the form the user will interact with
    """
    class Meta:
        model = Post
        fields = ['title', 'content', 'featured_image']