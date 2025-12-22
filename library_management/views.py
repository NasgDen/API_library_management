from django.template.context_processors import request
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.generics import CreateAPIView, DestroyAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView
from rest_framework.permissions import IsAdminUser

from library_management.models import Author, Book, BookIssuance
from library_management.paginations import BookPagination, AuthorPagination, BookIssuancePagination
from library_management.permissions import IsLibrarian, IsOwner
from library_management.serializers import AuthorSerializer, BookIssuanceSerializer, BookSerializer, BookListSerializer


class BookCreateApiView(CreateAPIView):
    """Класс реализует создание книги"""

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsLibrarian | IsAdminUser]

    def perform_create(self, serializer):
        """Функция записывает пользователя создавшего книгу"""

        serializer.save(owner=self.request.user)


class BookListApiView(ListAPIView):
    """Класс реализует отображение всех книг"""

    queryset = Book.objects.all()
    serializer_class = BookListSerializer
    pagination_class = BookPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ["title", "author__last_name", "year"]
    search_fields = ["title", "year", "author__last_name"]


class BookRetrieveAPIView(RetrieveAPIView):
    """Класс реализует отображение одной книги"""

    queryset = Book.objects.all()
    serializer_class = BookListSerializer


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

    def perform_create(self, serializer):
        """Функция записывает пользователя создавшего автора"""

        serializer.save(owner=self.request.user)


class AuthorListApiView(ListAPIView):
    """Класс реализует отображение всех авторов"""

    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    pagination_class = AuthorPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ["first_name", "last_name", "patronymic"]
    search_fields = ["first_name", "last_name", "patronymic"]


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

    def perform_create(self, serializer):
        """Функция записывает пользователя создавшего информацию о выдаче книги"""

        serializer.save(owner=self.request.user)


class BookIssuanceListApiView(ListAPIView):
    """Класс реализует просмотр списка всех выданных книг"""

    queryset = BookIssuance.objects.all()
    serializer_class = BookIssuanceSerializer
    pagination_class = BookIssuancePagination
    permission_classes = [IsLibrarian | IsAdminUser]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = [
        "book__title",
        "user__last_name",
        "user__email",
        "book_issued",
        "book_returned",
        "date_create",
        "date_return",
    ]
    search_fields = [
        "book__title",
        "user__last_name",
        "user__email",
        "book_issued",
        "book_returned",
        "date_create",
        "date_return",
    ]


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

    def perform_update(self, serializer):
        """Функция проверяет изменение, если статус - книга сдана True, то стасус - книга выдана - False"""

        book_issuance = serializer.save()
        if book_issuance.book_returned:
            book_issuance.book_issued = False
        book_issuance.save()


class BookIssuanceDestroyApiView(DestroyAPIView):
    """Класс реализует изменение информации о выданной книг"""

    queryset = BookIssuance.objects.all()
    permission_classes = [IsLibrarian | IsAdminUser]
