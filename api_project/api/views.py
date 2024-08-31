from django.shortcuts import render
from rest_framework import generics
from rest_framework import viewsets
from .models import book
from .serializers import BookSerializer
# Create your views here.

class BookList(generics.ListAPIView):
    queryset = book.objects.all()
    serializer_class = BookSerializer
class BookViewSet(viewsets.ModelViewSet):
    queryset = book.objects.all()
    serializer_class = BookSerializer

