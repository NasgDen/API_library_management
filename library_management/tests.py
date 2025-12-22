from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from datetime import date

from library_management.models import Book, Author
from users.models import User


class BookTestCase(APITestCase):
    """Класс реализует тесты"""

    def setUp(self):
        self.user = User.objects.create(email="test@email.com", username="test", phone="+79999999999", is_staff=True)
        self.client.force_authenticate(user=self.user)
        self.author = Author.objects.create(
            first_name="Александ", last_name="Пушкин", patronymic="Сергеевич", owner=self.user
        )
        self.book = Book.objects.create(title="Test", author=self.author, year="2025-01-01", owner=self.user)

    def test_book_retrieve(self):
        """Тест - детальный просмотр книги"""

        url = reverse("library_management:book_retrieve", args=(self.book.pk,))
        response = self.client.get(url)
        data = response.json()
        authors = {
            "first_name": "Александ",
            "last_name": "Пушкин",
            "patronymic": "Сергеевич",
            "owners": {
                "email": "test@email.com",
                "first_name": "",
                "last_name": "",
                "patronymic": None,
                "phone": "+79999999999",
            },
            "date_create": str(date.today()),
            "date_update": str(date.today()),
        }
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("title"), self.book.title)
        self.assertEqual(data.get("authors"), authors)
        self.assertEqual(data.get("year"), self.book.year)

    def test_book_create(self):
        """Тест - создание книги"""

        url = reverse("library_management:book_create")
        data = {
            "title": "Test2",
            "author": self.author.pk,
            "year": "2025-02-02",
        }
        response = self.client.post(url, data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.all().count(), 2)

    def test_book_update_patch(self):
        """Тест - Изменение информации о книге. Patch запрос"""

        url = reverse("library_management:book_update", args=(self.book.pk,))
        data = {
            "title": "Test 999",
        }
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_book_update_put(self):
        """Тест - Изменение информации о книге. Put запрос"""

        url = reverse("library_management:book_update", args=(self.book.pk,))
        data = {
            "title": "Test 123",
            "author": self.author.pk,
            "year": "2025-04-04",
        }
        response = self.client.put(url, data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("title"), "Test 123")

    def test_book_delete(self):
        """Тест - удаление информации о книги"""

        url = reverse("library_management:book_delete", args=(self.book.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.all().count(), 0)

    def test_book_list(self):
        """Тест - Просмотр списка книг"""

        url = reverse("library_management:book_list")
        response = self.client.get(url)
        data = response.json()
        result = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": 4,
                    "title": "Test",
                    "authors": {
                        "first_name": "Александ",
                        "last_name": "Пушкин",
                        "patronymic": "Сергеевич",
                        "owners": {
                            "email": "test@email.com",
                            "first_name": "",
                            "last_name": "",
                            "patronymic": None,
                            "phone": "+79999999999",
                        },
                        "date_create": str(date.today()),
                        "date_update": str(date.today()),
                    },
                    "year": "2025-01-01",
                    "owners": {
                        "email": "test@email.com",
                        "first_name": "",
                        "last_name": "",
                        "patronymic": None,
                        "phone": "+79999999999",
                    },
                    "date_create": str(date.today()),
                    "date_update": str(date.today()),
                }
            ],
        }
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Book.objects.all().count(), 1)
        self.assertEqual(data, result)
