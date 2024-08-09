# Delete a Book Instance


book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()  # Direct use of book.delete

Expected Output: <QuerySet []>

# The book "Nineteen Eighty-Four" was successfully deleted. The remaining books list is empty.
