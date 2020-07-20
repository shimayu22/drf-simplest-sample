from rest_framework import serializers
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from shop.models import Book
from .serializers import BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializers_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

