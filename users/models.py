from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    """Модель создания и регистрации пользователя"""
    email = models.EmailField(unique=True, verbose_name='Ваша почта')
    phone_number = models.CharField(max_length=11, blank=True, null=True)
    avatar = models.ImageField(upload_to='users/avatars/', blank=True, null=True, verbose_name='Фото(необязательно)')
    country = models.CharField(max_length=50, verbose_name='Страна проживания')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email
