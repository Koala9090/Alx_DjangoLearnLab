# users/views.py
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render


def is_Admin(user):
    return user.userprofile.role == 'Admin'

@user_passes_test(is_Admin)
def Admin_view(request):
    return render(request, 'admin_view.html')

def is_librarian(user):
    return user.userprofile.role == 'Librarian'

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'librarian_view.html')

def is_member(user):
    return user.userprofile.role == 'Member'

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'librarian_view.html')

@user_passes_test(is_member)
def member_view(request):
    return render(request, 'member_view.html')
