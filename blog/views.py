from django.shortcuts import render, get_object_or_404, reverse
from django.views.generic import ListView, View
from django.views.generic.detail import DetailView
from .models import Post

class HomepageView(ListView):
    '''
    Class-based view for homepage to show lists of posts
    '''
    model = Post
    queryset = Post.objects.order_by('-created_on')
    template_name = 'index.html'


class PostDetailedView(DetailView):
    model = Post
    template_name = 'post_detailed_view.html'