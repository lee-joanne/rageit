from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, View
from .models import Post


class PostView(ListView):
    '''
    Class-based view for homepage to show lists of posts
    '''
    model = Post
    queryset = Post.objects.order_by('-created_on')
    template_name = 'index.html'
