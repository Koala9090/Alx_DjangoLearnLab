from rest_framework import viewsets , permissions
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from .permissions import IsOwnerOrReadOnly
from accounts.models import CustomUser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

# Create your views here.
# Post ViewSet
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        # Set the author to the logged-in user
        serializer.save(author=self.request.user)

# Comment ViewSet
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        # Set the author to the logged-in user
        serializer.save(author=self.request.user)

class UserFeedView(APIView):
    permission_classes = [IsAuthenticated]  # Only authenticated users can view the feed

    def get(self, request):
        # Get the list of users that the current user is following
        current_user = request.user
        following_users = current_user.following.all()
        
        # Get all posts from users that the current user follows
        posts = Post.objects.filter(author__in=following_users).order_by('-created_at')
        
        # Serialize the posts to return them as JSON
        serializer = PostSerializer(posts, many=True)
        
        return Response(serializer.data)