# Import the Django settings and models
import os
import django

# Set up Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project_name.settings')
django.setup()

# Import the models
from .models import Author, Book, Library, Librarian

# Function to query all books by a specific author
def query_books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        books = Book.objects.filter(author=author)
        print(f"Books by {author_name}:")
        for book in books:
            print(f"- {book.title}")
    except Author.DoesNotExist:
        print(f"Author {author_name} does not exist.")

# Function to list all books in a library
def list_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()
        print(f"Books in {library_name}:")
        for book in books:
            print(f"- {book.title}")
    except Library.DoesNotExist:
        print(f"Library {library_name} does not exist.")

# Function to retrieve the librarian for a library
def retrieve_librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        librarian = library.librarian
        print(f"Librarian for {library_name}: {librarian.name}")
    except Library.DoesNotExist:
        print(f"Library {library_name} does not exist.")
    except Librarian.DoesNotExist:
        print(f"No librarian assigned to {library_name}.")

# Function to retrieve the librarian for a library using the library's field in Librarian
def retrieve_librarian_by_library(library_name):
    try:
        librarian = Librarian.objects.get(library="")
        print(f"Librarian for {library_name}: {librarian.name}")
    except Librarian.DoesNotExist:
        print(f"No librarian assigned to {library_name}.")
    except Library.DoesNotExist:
        print(f"Library {library_name} does not exist.")

if __name__ == "__main__":
    # Example usage
    author_name = "J.K. Rowling"
    library_name = "Central Library"
    
    print("\nQuerying Books by Author:")
    query_books_by_author(author_name)
    
    print("\nListing Books in Library:")
    list_books_in_library(library_name)
    
    print("\nRetrieving Librarian for Library (via Library object):")
    retrieve_librarian_for_library(library_name)
    
    print("\nRetrieving Librarian by Library field:")
    retrieve_librarian_by_library(library_name)



'''from models import Author,Book,Librarian,Library

library = Library.objects.get(name="Central Library")

# Get all books in this library
books_in_library = library.books.all()

# Print the titles of the books
for book in books_in_library:
    print(book.title)

# Assume you have an Author object
author = Author.objects.get(name="J.K. Rowling")

# Query all books by this author
books_by_author = Book.objects.filter(author=author)

# Print the titles of the books
for book in books_by_author:
    print(book.title)


book = Book.objects.create(title="Harry Potter", author=author)



# Retrieve the librarian for this library
librarian = library.librarian

# Print the librarian's name
print(librarian.name) '''
