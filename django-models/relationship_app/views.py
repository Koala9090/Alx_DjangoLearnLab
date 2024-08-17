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

from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log in the user after registration
            return redirect('list_books')  # Redirect to a success page or wherever you want
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
