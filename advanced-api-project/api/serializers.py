from rest_framework import serializers
from .models import Author, Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
    # Custom validation to ensure publication_year is not in the future
    def validate_publication_date(self, value):
        from datetime import date
        if value > date.now().year:
            raise serializers.ValidationError('Publication date cannot be in the future')
        return value
class AuthorSerializer (serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)
    class Meta:
        model = Author
        fields = ['name','books']
