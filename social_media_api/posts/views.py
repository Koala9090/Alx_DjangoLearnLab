from rest_framework import viewsets , permissions
from .models import Post, Comment,Like
from .serializers import PostSerializer, CommentSerializer
from .permissions import IsOwnerOrReadOnly
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from notifications.utils import create_notification
from rest_framework import generics
from notifications.models import Notification

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
    
# Like a post
class LikePostView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):  # Ensure we are using 'pk' as the variable name
        # Use generics.get_object_or_404 with 'pk' exactly as required
        post = generics.get_object_or_404(Post, pk=pk)
        
        # Get or create the like relationship between user and post
        like, created = Like.objects.get_or_create(user=request.user, post=post)
        
        if created:
            # Create a notification if a new like was created
            Notification.objects.create(
                recipient=post.author,
                actor=request.user,
                verb='liked',
                target=post
            )
            return Response({"message": "You liked this post."})
        else:
            return Response({"message": "You have already liked this post."})

# Unlike a post
class UnlikePostView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):  # Ensure we are using 'pk' as the variable name
        # Use generics.get_object_or_404 with 'pk' exactly as required
        post = generics.get_object_or_404(Post, pk=pk)
        
        # Check if the user has liked the post before
        like = Like.objects.filter(user=request.user, post=post).first()
        
        if like:
            # Delete the like if it exists
            like.delete()
            return Response({"message": "You unliked this post."})
        else:
            return Response({"message": "You haven't liked this post yet."})
def like_post(request, post_id):
    post = Post.objects.get(id=post_id)
    post.likes.add(request.user)  
    
    # Trigger notification
    create_notification(actor=request.user, recipient=post.author, verb="liked", target=post)
    
    return Response({"message": "You liked this post."})