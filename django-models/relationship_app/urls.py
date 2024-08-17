# users/urls.py
from django.urls import path
from .views import Admin_view, librarian_view, member_view

urlpatterns = [
    path('admin/', Admin_view, name='admin_view'),
    path('librarian/', librarian_view, name='librarian_view'),
    path('member/', member_view, name='member_view'),
]
