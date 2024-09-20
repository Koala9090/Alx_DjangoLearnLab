from django.urls import path
from .views import NotificationListView, UnreadNotificationListView

urlpatterns = [
    path('notifications/', NotificationListView.as_view(), name='notification-list'),
    path('notifications/unread/', UnreadNotificationListView.as_view(), name='unread-notifications'),
]
