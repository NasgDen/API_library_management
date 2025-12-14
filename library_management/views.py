from rest_framework.generics import CreateAPIView, ListAPIView

from library_management.models import Book
from library_management.serializers import BookSerializer


class BookCreateApiView(CreateAPIView):
    """ Класс реализует создание книги """

    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookListApiView(ListAPIView):
    """ Класс реализует отображение всех книг """

    queryset = Book.objects.all()
    serializer_class = BookSerializer