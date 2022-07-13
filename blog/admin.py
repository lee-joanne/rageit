from django.contrib import admin
from .models import Post, Comment

class PostAdmin(admin.ModelAdmin):
    """
    Class to prepopulate slug field. Taken from this website: https://learndjango.com/tutorials/django-slug-tutorial
    """
    list_display = ("title", "content",)
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Post, PostAdmin)
admin.site.register(Comment)