from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
import datetime

class Post(models.Model):
    """
    Post model class
    """
    title = models.CharField(max_length=250, null=False, blank=False, unique=True)
    slug = models.SlugField(null=True, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_author")
    updated_on = models.DateTimeField(auto_now=True)
    content = CKEditor5Field('Text', config_name='extends')
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(max_length=150)
    created_on = models.DateTimeField(default=datetime.datetime.now)
    #likes = models.ManyToManyField(User, related_name='blog_likes', blank=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        """String for representing Post object in admin"""
        return self.title

class Comment(models.Model):
    """
    Comment model class
    """
    pass