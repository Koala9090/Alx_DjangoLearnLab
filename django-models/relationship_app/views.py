from django.http import HttpResponse
from .models import Book
from django.views.generic import DetailView
from .models import Library
def list_books(request):
    books = Book.objects.all()
    book_list = [f"{book.title} by {book.author.name}" for book in books]
    response = "\n".join(book_list)
    return HttpResponse(response, content_type="text/plain")


class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
