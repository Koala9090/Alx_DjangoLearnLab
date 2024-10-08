from django.urls import path
from .views import register, profile, PostCreateView,  PostListView, PostDetailView, PostDeleteView, PostUpdateView,CommentCreateView, CommentUpdateView, CommentDeleteView,search_posts,PostByTagListView
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
#comments urls
    path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), name='add-comment'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='edit-comment'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='delete-comment'),

    path('search/', search_posts, name='search_posts'),
    path('tags/<slug:tag_slug>/', PostByTagListView.as_view(), name='posts-by-tag'),
]
