from django.shortcuts import render
from django.views import generic, View
from .models import Post, Comment


def blogmain_view(request):
    return render(request, "index.html")