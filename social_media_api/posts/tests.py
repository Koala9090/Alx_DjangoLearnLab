from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import Post
from django.contrib.auth.models import User

class LikePostTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='password')
        self.post = Post.objects.create(title="Test Post", content="Test Content", author=self.user)
        self.client.login(username='testuser', password='password')

    def test_like_post(self):
        url = reverse('like-post', kwargs={'pk': self.post.pk})
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.post.likes.count(), 1)

    def test_unlike_post(self):
        self.post.likes.add(self.user)  # Add like manually
        url = reverse('unlike-post', kwargs={'pk': self.post.pk})
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.post.likes.count(), 0)
