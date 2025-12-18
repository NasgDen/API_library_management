from django.shortcuts import render
from rest_framework.generics import CreateAPIView, DestroyAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny, IsAdminUser

from users.models import User
from users.permissions import IsUser
from users.serializers import UserSerializer


class UserCreateApiView(CreateAPIView):
    """Класс реализует создание пользователя"""

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        """Функция после создания пользователя делает его активным и хэширует пароль"""

        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()


class UserListApiView(ListAPIView):
    """Класс реализует просмотр списка пользователей"""

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]


class UserRetrieveApiView(RetrieveAPIView):
    """Класс реализует просмотр данных о пользователе"""

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser | IsUser]


class UserUpdateApiView(UpdateAPIView):
    """Класс реализует изменение данных о пользователе"""

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsUser]


class UserDestroyApiView(DestroyAPIView):
    """Класс реализует удаление данных пользователя"""

    queryset = User.objects.all()
    permission_classes = [IsAdminUser]