from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models


class User(AbstractBaseUser):
    username = None
    email = models.EmailField(
        max_length=100,
        unique=True,
        verbose_name="Электронная почта",
        help_text="Введите адрес электронной почты.",
    )
    phone = models.CharField(
        max_length=25,
        verbose_name="Телефон",
        help_text="Введите номер телефона.",
        blank=True,
        null=True,
    )
    city = models.CharField(
        max_length=50,
        verbose_name="Город",
        help_text="Введите город проживания",
        blank=True,
        null=True,
    )
    avatar = models.ImageField(
        upload_to="users/avatar",
        verbose_name="Аватар",
        help_text="Загрузите аватар.",
        blank=True,
        null=True,
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ("email",)
