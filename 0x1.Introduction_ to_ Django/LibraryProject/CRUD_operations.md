 # Django Book Model CRUD Operations

# Create a Book Instance

```python
from bookshelf.models import Book

book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
print(book)
Expected Output:<Book: 1984>

# The book "1984" by George Orwell was successfully created with the publication year 1949

# Retrieve a Book Instance

retrieved_book = Book.objects.get(title="1984")
print(retrieved_book)
Expected Output:<Book: 1984>

# The book "1984" was retrieved successfully, displaying the title, author, and publication year

# Update a Book Instance

book_to_update = Book.objects.get(title="1984")
book_to_update.title = "Nineteen Eighty-Four"
book_to_update.save()
print(book_to_update)
Expected Output: <Book: Nineteen Eighty-Four>

# The title of the book was successfully updated from "1984" to "Nineteen Eighty-Four".

# Delete a Book Instance

book_to_delete = Book.objects.get(title="Nineteen Eighty-Four")
book_to_delete.delete()

remaining_books = Book.objects.all()
print(remaining_books)
Expected Output: <QuerySet []>

#The book "Nineteen Eighty-Four" was successfully deleted. The remaining books list is empty.

