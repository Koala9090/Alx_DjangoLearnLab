# Retrieve a Book Instance

retrieved_book = Book.objects.get(title="1984")
print(retrieved_book)
Expected Output:<Book: 1984>

# The book "1984" was retrieved successfully, displaying the title, author, and publication year
