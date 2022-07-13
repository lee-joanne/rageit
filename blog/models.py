from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from tinymce.models import HTMLField
import datetime

class Post(models.Model):
    """
    Post model class
    """
    title = models.CharField(max_length=250, null=False, blank=False, unique=True)
    slug = models.SlugField(null=True, unique=True, max_length=150)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_author")
    revised_on = models.DateTimeField(auto_now=True)
    content = HTMLField()
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(max_length=150)
    created_on = models.DateTimeField(auto_now=True )
    likes = models.ManyToManyField(User, related_name='blog_likes', blank=True)

    def get_absolute_url(self):
        return f"/post/{self.slug}"

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        """String for representing Post object in admin"""
        return self.title

    def number_of_likes(self):
        return self.likes.count()

    def number_of_comments(self):
        return self.post_comment.count()


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
