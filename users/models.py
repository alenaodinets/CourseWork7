from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name="Почта")
    phone = models.CharField(
        max_length=35, verbose_name="Телефон", blank=True, null=True
    )
    telegram_chat_id = models.CharField(
        max_length=50,
        unique=True,
        verbose_name="Telegram_chat_id",
        blank=True,
        null=True,
    )
    country = models.CharField(
        max_length=100, verbose_name="Страна", blank=True, null=True
    )
    city = models.CharField(max_length=100, verbose_name="Город", blank=True, null=True)
    avatar = models.ImageField(
        upload_to="users/", verbose_name="Аватар", blank=True, null=True
    )
    verification_code = models.CharField(
        max_length=10, verbose_name="Код верификации", blank=True, null=True
    )
    last_login = models.DateTimeField(
        blank=True, null=True, verbose_name="Дата последнего входа"
    )
    is_active = models.BooleanField(default=False, verbose_name="Активен")
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.email}"

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ("email",)
