from django.shortcuts import render
from rest_framework import generics
from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticated, BasePermission
# Create your views here.

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes =[IsAuthenticated]

class IsBookOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user

