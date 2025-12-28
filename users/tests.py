from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from users.models import User


class UserTestCase(APITestCase):
    """Класс реализует тесты для модели User"""

    def setUp(self):
        self.user = User.objects.create(email="test@mail.ru", username="test", phone="+79999999999", is_staff=True)
        self.client.force_authenticate(user=self.user)

    def test_user_retrieve(self):
        """Тест - детальный просмотр информации о пользователе"""

        url = reverse("users:user_retrieve", args=(self.user.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("username"), self.user.username)
        self.assertEqual(data.get("email"), self.user.email)
        self.assertEqual(data.get("phone"), self.user.phone)

    def test_user_create(self):
        """Тест - создание пользователя"""

        url = reverse("users:user_create")
        data = {
            "email": "user@mail.ru",
            "username": "user",
            "password": "12345",
            "first_name": "Иван",
            "last_name": "Иванов",
            "patronymic": "Иванович",
            "phone": "+77777777777",
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.all().count(), 2)
        self.assertEqual(data.get("email"), "user@mail.ru")
        self.assertEqual(data.get("first_name"), "Иван")

    def test_user_patch_update(self):
        """Тест - Изменение информации о пользователе. Patch запрос"""

        url = reverse("users:user_update", args=(self.user.pk,))
        data = {
            "first_name": "Петр",
        }
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("first_name"), "Петр")

    def test_user_put_update(self):
        """Тест - Изменение информации о пользователе. Put запрос"""

        url = reverse("users:user_update", args=(self.user.pk,))
        data = {
            "email": "user1@mail.ru",
            "username": "user1",
            "password": "54321",
            "first_name": "Петр",
            "last_name": "Петров",
            "patronymic": "Петрович",
            "phone": "+78888888888",
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("email"), "user1@mail.ru")
        self.assertEqual(data.get("username"), "user1")
        self.assertEqual(data.get("first_name"), "Петр")
        self.assertEqual(data.get("last_name"), "Петров")
        self.assertEqual(data.get("patronymic"), "Петрович")
        self.assertEqual(data.get("phone"), "+78888888888")

    def test_user_list(self):
        """Тест - Просмотр списка пользователей"""

        url = reverse("users:user_list")
        response = self.client.get(url)
        data = response.json()
        result = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": 29,
                    "password": "",
                    "last_login": None,
                    "is_superuser": False,
                    "username": "test",
                    "is_staff": True,
                    "is_active": True,
                    "date_joined": data.get("results")[0].get("date_joined"),
                    "email": "test@mail.ru",
                    "first_name": "",
                    "last_name": "",
                    "patronymic": None,
                    "phone": "+79999999999",
                    "avatar": None,
                    "groups": [],
                    "user_permissions": [],
                }
            ],
        }
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, result)

    def test_user_delete(self):
        """Тест - удаление пользователя"""

        url = reverse("users:user_delete", args=(self.user.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(User.objects.all().count(), 0)
