from rest_framework.generics import CreateAPIView, DestroyAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView
from rest_framework.permissions import IsAdminUser

from library_management.models import Author, Book, BookIssuance
from library_management.permissions import IsLibrarian, IsOwner
from library_management.serializers import AuthorSerializer, BookIssuanceSerializer, BookSerializer


class BookCreateApiView(CreateAPIView):
    """Класс реализует создание книги"""

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsLibrarian | IsAdminUser]


class BookListApiView(ListAPIView):
    """Класс реализует отображение всех книг"""

    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookRetrieveAPIView(RetrieveAPIView):
    """Класс реализует отображение одной книги"""

    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookUpdateApiView(UpdateAPIView):
    """Класс реализует изменение данных о книге"""

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsOwner | IsAdminUser]


class BookDestroyApiView(DestroyAPIView):
    """Класс реализует удаление данных о книге"""

    queryset = Book.objects.all()
    permission_classes = [IsOwner | IsAdminUser]


class AuthorCreateApiView(CreateAPIView):
    """Класс реализует создание автора"""

    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsLibrarian | IsAdminUser]


class AuthorListApiView(ListAPIView):
    """Класс реализует отображение всех авторов"""

    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorRetrieveApiView(RetrieveAPIView):
    """Класс реализует просмотр данных об одном авторе"""

    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorUpdateApiView(UpdateAPIView):
    """Класс реализует изменение данных об авторе"""

    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsOwner | IsAdminUser]


class AuthorDestroyApiView(DestroyAPIView):
    """Класс реализует удаление данных об авторе"""

    queryset = Author.objects.all()
    permission_classes = [IsOwner | IsAdminUser]


class BookIssuanceCreateApiView(CreateAPIView):
    """Класс реализует создание информации о выдачи книги"""

    queryset = BookIssuance.objects.all()
    serializer_class = BookIssuanceSerializer
    permission_classes = [IsLibrarian | IsAdminUser]


class BookIssuanceListApiView(ListAPIView):
    """Класс реализует просмотр списка всех выданных книг"""

    queryset = BookIssuance.objects.all()
    serializer_class = BookIssuanceSerializer
    permission_classes = [IsLibrarian | IsAdminUser]


class BookIssuanceRetrieveApiView(RetrieveAPIView):
    """Класс реализует просмотр информации о выданной книге"""

    queryset = BookIssuance.objects.all()
    serializer_class = BookIssuanceSerializer
    permission_classes = [IsLibrarian | IsAdminUser]


class BookIssuanceUpdateApiView(UpdateAPIView):
    """Класс реализует изменение информации о выданной книг"""

    queryset = BookIssuance.objects.all()
    serializer_class = BookIssuanceSerializer
    permission_classes = [IsLibrarian | IsAdminUser]


class BookIssuanceDestroyApiView(DestroyAPIView):
    """Класс реализует изменение информации о выданной книг"""

    queryset = BookIssuance.objects.all()
    permission_classes = [IsLibrarian | IsAdminUser]
