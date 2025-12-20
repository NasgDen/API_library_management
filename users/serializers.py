from rest_framework.serializers import ModelSerializer

from users.models import User
from users.validators import PhoneValidator


class UserSerializer(ModelSerializer):
    """Класс сериализатора для модели User"""

    class Meta:
        model = User
        fields = "__all__"
        validators = [PhoneValidator(field="phone"),]


class UserBasicSerializer(ModelSerializer):
    """ Класс сериализатора для модели User c базовыми полями """

    class Meta:
        model = User
        fields = (
            "email",
            "first_name",
            "last_name",
            "patronymic",
            "phone"
        )