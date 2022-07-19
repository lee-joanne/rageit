from . import views
from django.urls import path

urlpatterns = [
    path('', views.HomepageView.as_view(), name='homepage'),
    path('create_post/', views.CreatePostView.as_view(), name='create_post'),
    path('<slug:slug>/', views.PostDetailedView.as_view(), name='post_detailed_view'),
]