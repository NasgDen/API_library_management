from rest_framework.serializers import ModelSerializer

from users.models import User


class UserSerializer(ModelSerializer):
    """Класс сериалайзер для модели User"""

    class Meta:
        model = User
        fields = "__all__"


class UserBasicSerializer(ModelSerializer):
    """ Класс сериалайзер для модели User c базовыми полями """

    class Meta:
        model = User
        fields = (
            "email",
            "first_name",
            "last_name",
            "patronymic",
            "phone"
        )