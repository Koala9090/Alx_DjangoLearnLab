from django.urls import path 
from . import views
from .views import (
    PostCreateView,PostListView,PostDetailView,PostUpdateView,PostDeleteView
)
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', PostListView.as_view(), name='home'),  # Home page (could be the same as posts)
    path('posts/', PostListView.as_view(), name='post_list'),
    path('login/',auth_views.LoginView.as_view(template_name='blog/login.html'),name='login'),
    path('loguot/',auth_views.LogoutView.as_view(),name='logout'),
    path('register/',views.register,name='register'),
    path('profile/',views.profile,name='profile'),
    path('post/<int:pk>/',PostDetailView.as_view(), name='post_detail'),
    path('post/new/',PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/edit/',PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/',PostDeleteView.as_view(), name='post_delete'),
]