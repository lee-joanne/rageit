from django.contrib import admin
from django import forms
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    prepopulated_slug_fields = {'slug': ('title',)}
    prepopulated_excerpt_fields = {'excerpt': ('content',)}
