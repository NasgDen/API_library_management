from rest_framework.serializers import ModelSerializer, SerializerMethodField

from library_management.models import Author, Book, BookIssuance
from users.serializers import UserSerializer, UserBasicSerializer


class AuthorSerializer(ModelSerializer):
    """Класс сериализатор для модели Author"""

    owners = UserBasicSerializer(source="owner", many=False, read_only=True)

    class Meta:
        model = Author
        fields = (
            "first_name",
            "last_name",
            "patronymic",
            "owners",
            "date_create",
            "date_update"
        )


class BookSerializer(ModelSerializer):
    """Класс сериализатор для модели Book"""

    authors = AuthorSerializer(source="author", many=False, read_only=True)
    owners = UserBasicSerializer(source="owner", many=False, read_only=True)

    class Meta:
        model = Book
        fields = (
            "id",
            "title",
            "authors",
            "year",
            "owners",
            "date_create",
            "date_update"
        )


class BookIssuanceSerializer(ModelSerializer):
    """Класс сериализатор для модели BookIssuance"""

    class Meta:
        model = BookIssuance
        fields = "__all__"
