from django.urls import path
from . import views

urlpatterns = [
    path('books/add/', views.add_book, name='add_book'),
    path('books/<int:book_id>/edit/', views.edit_book, name='edit_book'),
    path('books/<int:book_id>/delete/', views.delete_book, name='delete_book'),
    # Other URL patterns for your app
]


# from django.urls import path
# from . import views

# urlpatterns = [
#     path('admin-view/', views.admin_view, name='admin_view'),
#     path('librarian-view/', views.librarian_view, name='librarian_view'),
#     path('member-view/', views.member_view, name='member_view'),
# ]


# from django.urls import path
# from . import views
# from django.contrib.auth import views as auth_views
# from .views import list_books
# from django.urls import path
# from . import views  # Import all views from the current module
# from .views import list_books, LibraryDetailView  # Import specific views

# urlpatterns = [
#     path('books/', list_books, name='list_books'),  # Function-based view
#     path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  # Class-based view
# ]

# urlpatterns = [
#     path('login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
#     path('logout/', auth_views.LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
#     path('register/', views.register, name='register'),
#     # Other URL patterns for your app
# ]
