# Update a Book Instance

book_to_update = Book.objects.get(title="1984")
book_to_update.title = "Nineteen Eighty-Four"
book_to_update.save()
print(book_to_update.title)  
Expected Output: <Book: Nineteen Eighty-Four>

# The title of the book was successfully updated from "1984" to "Nineteen Eighty-Four".
