from django.shortcuts import render
from .models import Book , Library
# Create your views here.
def list_books(request):
    books = Book.objects.all()
    return render(request, 'list_books.html', {'books': books})

class libraryDetailView(DetailView):
    model=Library
    template_name = 'library_detail.html'
    contextr_object_name = 'library'


