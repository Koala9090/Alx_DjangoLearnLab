from django.urls import path
from . import views  # Import all views from the current module
from .views import list_books, LibraryDetailView  # Import specific views

urlpatterns = [
    path('books/', list_books, name='list_books'),  # Function-based view
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  # Class-based view
]
