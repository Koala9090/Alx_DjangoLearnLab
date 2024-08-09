# Update a Book Instance

book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
print(book.title)  # book.title is used here directly
print(book_to_update.title)  
Expected Output: Nineteen Eighty-Four

# The title of the book was successfully updated from "1984" to "Nineteen Eighty-Four".
