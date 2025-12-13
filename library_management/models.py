from django.db import models

from config import settings


class Author(models.Model):
    """Описание полей модели - Автор"""

    first_name = models.CharField(max_length=30, verbose_name="Имя автора", help_text="Укажите Имя автора")
    last_name = models.CharField(max_length=30, verbose_name="Фамилия автора", help_text="Укажите Фамилию автора")
    patronymic = models.CharField(
        max_length=30, verbose_name="Отчество автора", help_text="Укажите Отчество автора", blank=True, null=True
    )
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="Владелец",
        help_text="Укажите владельца",
        related_name="book+",
        blank=True,
        null=True,
    )
    date_create = models.DateField(auto_now_add=True, verbose_name="Дата создания записи об авторе")
    date_update = models.DateField(auto_now=True, verbose_name="Дата изменения записи об авторе")

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.patronymic}"

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"


class Book(models.Model):
    """Описание полей модель - Книга"""

    title = models.CharField(max_length=150, verbose_name="Название", help_text="Укажите название")
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        verbose_name="Автор",
        help_text="Укажите автора",
        related_name="book+",
    )
    year = models.DateField(verbose_name="Дата выхода книги", help_text="Укажите дату выхода книги")
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="Владелец",
        help_text="Укажите владельца",
        related_name="book+",
        blank=True,
        null=True,
    )
    date_create = models.DateField(auto_now_add=True, verbose_name="Дата создания записи о книге")
    date_update = models.DateField(auto_now=True, verbose_name="Дата изменения записи о книге")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"
