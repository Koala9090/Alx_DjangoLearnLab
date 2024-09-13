from django.urls import path
from .views import register, profile, PostListView,  PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from django.contrib.auth.views import LogoutView
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('register/', register, name='register'),
    path('profile/', profile, name='profile_update'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('post/', PostListView.as_view(), name='post_list'),       # List all posts
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),  # View a specific post
    path('post/new/', PostCreateView.as_view(), name='post_create'),  # Create a new post
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post_edit'),  # Edit an existing post
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),  # Delete a post
]