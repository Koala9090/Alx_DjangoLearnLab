from rest_framework import generics, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from .serializers import UserSerializer, UserProfileSerializer
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from .models import CustomUser

User = get_user_model()

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserSerializer

class CustomObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })

class UserProfileView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        return self.request.user
    

    # View to follow a user
class FollowUserView(APIView):
    permission_classes = [IsAuthenticated]  # Ensure only authenticated users can follow others

    def post(self, request, username):
        # Get the user to follow
        user_to_follow = get_object_or_404(CustomUser, username=username)
        
        # The current user (the one making the request)
        current_user = request.user
        
        # Prevent a user from following themselves
        if current_user == user_to_follow:
            return Response({"detail": "You cannot follow yourself."}, status=status.HTTP_400_BAD_REQUEST)
        
        # Add the user to the following list
        current_user.following.add(user_to_follow)
        
        return Response({"detail": f"You are now following {user_to_follow.username}."}, status=status.HTTP_200_OK)

# View to unfollow a user
class UnfollowUserView(APIView):
    permission_classes = [IsAuthenticated]  # Ensure only authenticated users can unfollow others

    def post(self, request, username):
        # Get the user to unfollow
        user_to_unfollow = get_object_or_404(CustomUser, username=username)
        
        # The current user (the one making the request)
        current_user = request.user
        
        # Prevent a user from unfollowing themselves
        if current_user == user_to_unfollow:
            return Response({"detail": "You cannot unfollow yourself."}, status=status.HTTP_400_BAD_REQUEST)
        
        # Remove the user from the following list
        current_user.following.remove(user_to_unfollow)
        
        return Response({"detail": f"You have unfollowed {user_to_unfollow.username}."}, status=status.HTTP_200_OK)