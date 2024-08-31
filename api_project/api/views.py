from django.shortcuts import render
from rest_framework import generics
from rest_framework import viewsets
from .models import book
from .serializers import BookSerializer
# Create your views here.

class BookViewSet(viewsets.ModelViewSet):
    queryset = book.objects.all()
    serializer_class = BookSerializer

