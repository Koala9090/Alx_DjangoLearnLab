from django.urls import path
from . import views
from django.contrib.auth.decorators import permission_required

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    
    path('add_book/', permission_required('relationship_app.can_add_book')(views.add_book), name='add_book'),

    path('edit_book/<int:pk>/', permission_required('relationship_app.can_change_book')(views.edit_book), name='edit_book'),

    path('delete_book/<int:pk>/', permission_required('relationship_app.can_delete_book')(views.delete_book), name='delete_book'),
    
    # Other URL patterns
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
