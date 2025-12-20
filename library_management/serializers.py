from rest_framework.serializers import ModelSerializer, SerializerMethodField

from library_management.models import Author, Book, BookIssuance


class AuthorSerializer(ModelSerializer):
    """Класс сериализатор для модели Author"""

    class Meta:
        model = Author
        fields = "__all__"


class BookSerializer(ModelSerializer):
    """Класс сериализатор для модели Book"""

    authors = AuthorSerializer(source="author", many=False, read_only=True)

    class Meta:
        model = Book
        fields = (
            "id",
            "title",
            "authors",
            "year",
            "owner",
            "date_create",
            "date_update"
        )


class BookIssuanceSerializer(ModelSerializer):
    """Класс сериализатор для модели BookIssuance"""

    class Meta:
        model = BookIssuance
        fields = "__all__"
