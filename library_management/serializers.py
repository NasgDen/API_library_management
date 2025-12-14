from rest_framework.serializers import ModelSerializer

from library_management.models import Book, Author


class BookSerializer(ModelSerializer):
    """ Класс сериализатор для модели Book """

    class Meta:
        model = Book
        fields = "__all__"


class AuthorSerializer(ModelSerializer):
    """ Класс сериализатор для модели Author """

    class Meta:
        model = Author
        fields = "__all__"
