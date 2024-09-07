from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Book
from django.contrib.auth.models import User


class BookTests(APITestCase):

    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')

      
        self.book = Book.objects.create(title="Test Book", author="Author Name", publication_year=2022)

    def test_create_book(self):
        url = reverse('book-list')  
        data = {'title': 'New Book', 'author': 'New Author', 'publication_year': 2023}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)
        self.assertEqual(Book.objects.get(id=2).title, 'New Book')

    def test_retrieve_book(self):
        url = reverse('book-detail', kwargs={'pk': self.book.pk})  
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Test Book')

    def test_update_book(self):
        url = reverse('book-detail', kwargs={'pk': self.book.pk})
        data = {'title': 'Updated Book', 'author': 'Updated Author', 'publication_year': 2021}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, 'Updated Book')

    def test_delete_book(self):
        url = reverse('book-detail', kwargs={'pk': self.book.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    def test_filter_books_by_author(self):
        url = reverse('book-list') + '?author=Author Name'  
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_search_books(self):
        url = reverse('book-list') + '?search=Test'  
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_order_books(self):
        url = reverse('book-list') + '?ordering=-publication_year'  
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], 'Test Book')
    def test_unauthorized_access(self):
        self.client.logout()  # Ensure no user is logged in
        url = reverse('book-detail', kwargs={'pk': self.book.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

