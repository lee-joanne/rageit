from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from cloudinary.models import CloudinaryField
from tinymce.models import HTMLField
from datetime import datetime
from django.template.defaultfilters import slugify

class Post(models.Model):
    """
    Post model class
    """
    title = models.CharField(max_length=250, null=False, blank=False, unique=True)
    slug = models.SlugField(null=False, unique=True, max_length=150)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_author")
    content = HTMLField()
    featured_image = CloudinaryField('image', default='placeholder')
    likes = models.ManyToManyField(User, related_name='blog_likes', blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    revised_on = models.DateTimeField(auto_now=True)

    class Meta:
        """
        Class to set the order of the posts.
        """
        ordering = ['-created_on']

    def __str__(self):
        """
        Function to create the string for representing Post object in admin
        """
        return self.title

    def number_of_likes(self):
        """
        Function to return the number of likes of post
        """
        return self.likes.count()

    def number_of_comments(self):
        """
        Function to return number of comments of post
        """
        return self.post_comment.count()

    def get_absolute_url(self):
        """
        Creates url from slug field. Code taken from https://learndjango.com/tutorials/django-slug-tutorial
        """
        return reverse("postdetailedview", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        """
        Autopopulates slug when user creates new posts. Code taken from https://learndjango.com/tutorials/django-slug-tutorial
        """
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)


class Comment(models.Model):
    """
    Comment model class
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="post_comment")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comment_author")
    content = HTMLField()
    created_on = models.DateTimeField(auto_now=True)
    revised_on = models.DateTimeField(auto_now=True)
    featured_image = CloudinaryField('image', default='placeholder')
    comment_likes = models.ManyToManyField(User, related_name='comment_likes', blank=True)

    def number_of_comment_likes(self):
        return self.comment_likes.count()
    
    class Meta:
        ordering = ['created_on']
    
    def __str__(self):
        """String for representing Post object in admin"""
        return f"Comment by {self.author}"
