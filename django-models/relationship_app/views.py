
from django.shortcuts import render
from .models import Book
from django.views.generic import DetailView
from .models import Library

def list_books(request):
    """Display a list of all books."""
    books = Book.objects.all()  
    return render(request, 'list_books.html', {'books': books})

class LibraryDetailView(DetailView):
    """Display details for a specific library."""
    model = Library 
    template_name = 'library_detail.html'
    context_object_name = 'library'
