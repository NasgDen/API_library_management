from rest_framework.generics import CreateAPIView, ListAPIView

from library_management.models import Book, Author
from library_management.serializers import BookSerializer, AuthorSerializer


class BookCreateApiView(CreateAPIView):
    """ Класс реализует создание книги """

    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookListApiView(ListAPIView):
    """ Класс реализует отображение всех книг """

    queryset = Book.objects.all()
    serializer_class = BookSerializer


class AuthorCreateApiView(CreateAPIView):
    """ Класс реализует создание автора """

    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorListApiView(ListAPIView):
    """ Класс реализует отображение всех авторов """

    queryset = Author.objects.all()
    serializer_class = AuthorSerializer