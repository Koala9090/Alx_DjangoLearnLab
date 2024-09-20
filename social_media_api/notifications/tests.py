from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from posts.models import Post
from .models import Notification
from django.contrib.auth.models import User

class NotificationTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='password')
        self.post = Post.objects.create(title="Test Post", content="Test Content", author=self.user)
        self.client.login(username='testuser', password='password')

    def test_receive_like_notification(self):
        # Simulate liking a post
        url = reverse('like-post', kwargs={'pk': self.post.pk})
        self.client.post(url)
        
        # Check if notification is created
        notifications = Notification.objects.filter(recipient=self.user)
        self.assertEqual(notifications.count(), 1)
        self.assertEqual(notifications.first().verb, "liked")

