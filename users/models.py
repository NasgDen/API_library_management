from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Модель Пользователь"""

    email = models.EmailField(unique=True, help_text="Укажите электронную почту")
    first_name = models.CharField(max_length=30, verbose_name="Имя пользователя", help_text="Укажите Имя пользователя")
    last_name = models.CharField(
        max_length=30, verbose_name="Фамилия пользователя", help_text="Укажите Фамилию пользователя"
    )
    patronymic = models.CharField(
        max_length=30,
        verbose_name="Отчество пользователя",
        help_text="Укажите Отчество пользователя",
        blank=True,
        null=True,
    )
    phone = models.CharField(
        max_length=150, verbose_name="Номер телефона", help_text="Укажите номер телефона", blank=True, null=True
    )
    avatar = models.ImageField(
        upload_to="users/avatar/", verbose_name="Аватар", help_text="Укажите авара", blank=True, null=True
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
