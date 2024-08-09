# Delete a Book Instance

book_to_delete = Book.objects.get(title="Nineteen Eighty-Four")
book_to_delete.delete()

remaining_books = Book.objects.all()
print(remaining_books)
Expected Output: <QuerySet []>

# The book "Nineteen Eighty-Four" was successfully deleted. The remaining books list is empty.
