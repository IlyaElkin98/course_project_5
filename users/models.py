from django.contrib.auth.models import AbstractUser
from django.db import models
from .managers import UserManager

class User(AbstractUser):
    """Модель пользователя"""
    username = None
    email = models.EmailField(max_length=100, verbose_name='Электронная почта',
                              help_text='Введите адрес электронной почты', unique=True)
    phone = models.CharField(max_length=15, verbose_name='Номер телефона')
    city = models.CharField(max_length=100, verbose_name='Город проживания')
    tg_chat_id = models.CharField(max_length=50, blank=True, null=True, verbose_name='Телеграм чат id')

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ["email"]