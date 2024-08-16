# Create a Book Instance

```python
from bookshelf.models import Book

book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
print(book)
Expected Output:<Book: 1984>

# The book "1984" by George Orwell was successfully created with the publication year 1949
