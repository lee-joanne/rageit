from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Post


class PostView(generic.ListView):
    '''
    Class-based view for homepage to show lists of posts
    '''
    model = Post
    queryset = Post.objects.order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 8



