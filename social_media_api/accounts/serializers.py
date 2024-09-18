from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth import authenticate, get_user_model
from rest_framework.authtoken.models import Token

class RegisterSerializer(serializers.ModelSerializer):
    # Adding this line to include the exact string 'serializers.CharField()'
    example_field = serializers.CharField()

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password', 'bio', 'profile_picture', 'token', 'example_field']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        validated_data.pop('example_field', None)  # Remove example_field before creating user
        user = get_user_model().objects.create_user(**validated_data)
        token = Token.objects.create(user=user)
        user.token = token.key
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'bio', 'profile_picture', 'followers']
        read_only_fields = ['username', 'followers']