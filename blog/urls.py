from . import views
from django.urls import path

urlpatterns = [
    path('', views.HomepageView.as_view(), name='homepage'),
    path('<slug:slug>', views.PostDetailedView.as_view(), name='postdetailedview'),
]