from django.shortcuts import render, get_object_or_404, reverse
from django.views.generic import ListView, View
from django.core.exceptions import PermissionDenied
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from .models import Post, Comment
from .forms import PostForm, CommentForm
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
            'comment_form': CommentForm(),
            'liked': liked,
            'is_revised': post.created_on.strftime("%d, %m, %y") != post.revised_on.strftime("%d, %m, %y"),
        })

    def post(self, request, slug):
        """
        Function to allow users to create comments in detailed-post view
        """
        post = get_object_or_404(Post, slug=slug)
        post_comment = post.post_comment.order_by('created_on')
        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.author = self.request.user
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "post_detailed_view.html",
            {
                "post": post,
                "slug": slug,
                'post_comment': post_comment,
                "commented": True,
                "comment_form": CommentForm(),
            },
        )


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

    #Code on url permission access validation is taken from DamianJacob: https://github.com/Damianjacob
    def get(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        user = request.user
        if str(user.username) != str(post.author):
            raise PermissionDenied
        else:
            return render(request, 'update_post.html', {
                'post': post,
                'slug': slug
            })


class DeletePostView(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    """
    Class-based view for users to delete their posts
    """
    login_url = '/accounts/login/'
    model = Post
    template_name = 'delete_post.html'
    success_url = "/"
    success_message = "Your post is successfully deleted"

    #Code on url permission access validation is taken from DamianJacob: https://github.com/Damianjacob
    def get(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        user = request.user
        if str(user.username) != str(post.author):
            raise PermissionDenied
        else:
            return render(request, 'delete_post.html', {
                'post': post,
                'slug': slug
            })

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(DeletePostView, self).delete(request, *args, **kwargs)