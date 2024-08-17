from django.urls import path
from .views import list_books, lbrandDetailView

urlpatterns = [
    path('books', list_books, name='list_books'),
    path('library/<int:pk>/', lbrandDetailView.as_view(), name='library_detail'),
]
