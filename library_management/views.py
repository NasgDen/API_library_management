from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView

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


class BookRetrieveAPIView(RetrieveAPIView):
    """ Класс реализует отображение одной книги """

    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookUpdateApiView(UpdateAPIView):
    """ Класс реализует изменение данных о книге """

    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDestroyApiView(DestroyAPIView):
    """ Класс реализует удаление данных о книге """

    queryset = Book.objects.all()


class AuthorCreateApiView(CreateAPIView):
    """ Класс реализует создание автора """

    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorListApiView(ListAPIView):
    """ Класс реализует отображение всех авторов """

    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorRetrieveApiView(RetrieveAPIView):
    """ Класс реализует просмотр данных об одном авторе """

    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorUpdateApiView(UpdateAPIView):
    """ Класс реализует изменение данных об авторе """

    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorDestroyApiView(DestroyAPIView):
    """ Класс реализует удаление данных об авторе """

    queryset = Author.objects.all()