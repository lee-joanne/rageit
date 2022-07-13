from django.shortcuts import render, get_object_or_404, reverse
from django.views.generic import ListView, View
from django.views.generic.detail import DetailView
from .models import Post
from datetime import datetime
from time import strftime

class HomepageView(ListView):
    '''
    Class-based view for homepage to show lists of posts
    '''
    model = Post
    queryset = Post.objects.order_by('-created_on')
    template_name = 'index.html'
    created_date = datetime.strftime(Post.created_on, "%d %B, %Y")
    revised_date = datetime.strftime(Post.revised_on, "%d %B, %Y")


class PostView():
    pass