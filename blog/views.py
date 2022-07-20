from django.shortcuts import render, get_object_or_404, reverse
from django.views.generic import ListView, View
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post
from .forms import PostForm
from datetime import datetime


class HomepageView(ListView):
    '''
    Class-based view for homepage to show lists of posts
    '''
    model = Post
    queryset = Post.objects.order_by('-created_on')
    template_name = 'index.html'


class PostDetailedView(DetailView):
    """
    Class-based view to show detailed view of individual posts
    """
    model = Post
    template_name = 'post_detailed_view.html'

    def get(self, request, slug):
        queryset = Post.objects
        post = get_object_or_404(queryset, slug=slug)
        post_comment = post.post_comment.order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True
        
        return render(request, 'post_detailed_view.html', {
            'post': post,
            'slug': slug,
            'post_comment': post_comment,
            'liked': liked,
            'is_revised': post.created_on.strftime("%d, %m, %y") != post.revised_on.strftime("%d, %m, %y"),
        })


class CreatePostView(LoginRequiredMixin, CreateView):
    """
    Class-based for users to create new posts and have it saved
    """
    login_url = '/accounts/login/'
    model = Post
    template_name = 'create_post.html'
    form_class = PostForm
    success_url = "/"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
