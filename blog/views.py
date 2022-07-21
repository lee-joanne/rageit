from django.shortcuts import render, get_object_or_404, reverse
from django.views.generic import ListView, View
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
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


class CreatePostView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    """
    Class-based view for users to create new posts and have it saved
    """
    login_url = '/accounts/login/'
    model = Post
    template_name = 'create_post.html'
    form_class = PostForm
    success_url = "/"
    success_message = "Your post is now live! Check it out!"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class EditPostView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    """
    Class-based view for users to be able to edit posts they have made
    """
    login_url = '/accounts/login/'
    model = Post
    template_name = 'update_post.html'
    form_class = PostForm
    success_url = "/"
    success_message = "Your changes are now updated!"


class DeletePostView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    """
    Class-based view for users to delete their posts
    """
    login_url = '/accounts/login/'
    model = Post
    template_name = 'delete_post.html'
    success_url = "/"
    success_message = "Your post is successfully deleted"

