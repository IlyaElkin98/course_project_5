from django.contrib.auth.models import AbstractUser
from django.db import models
from .managers import UserManager

class User(AbstractUser):
    """Модель пользователя"""
    email = models.EmailField(max_length=100, verbose_name='Электронная почта',
                              help_text='Введите адрес электронной почты', unique=True)
    phone = models.CharField(max_length=15, verbose_name='Номер телефона')
    city = models.CharField(max_length=100, verbose_name='Город проживания')

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ["email"]