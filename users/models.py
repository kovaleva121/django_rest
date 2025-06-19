from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    email = models.EmailField(unique=True, verbose_name='Почта', help_text='Введите вашу почту')
    phone = models.CharField(max_length=35, verbose_name='Телефон', help_text='Укажите телефон')
    city = models.CharField(max_length=50, verbose_name='Город', help_text='Укажите свой город')
    avatar = models.ImageField(upload_to='users/avatar',blank=True, null=True, verbose_name='Аватар', help_text='Загрузите аватар')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email


