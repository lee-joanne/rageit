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
    created_date = Post.created_on.strftime("%d-%m-%y")
    revised_date = Post.revised_on.strftime("%d-%m-%y")


class PostView():
    pass