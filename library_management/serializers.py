from rest_framework.serializers import ModelSerializer

from library_management.models import Book


class BookSerializer(ModelSerializer):
    """ Класс сериализатор для модели Book """

    class Meta:
        models = Book
        fields = "__all__"
