from django.contrib.auth.models import AbstractUser
from django.db import models

from materials.models import Course, Lesson


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='Почта', help_text='Введите вашу почту')
    phone = models.CharField(max_length=35, verbose_name='Телефон', help_text='Укажите телефон', blank=True, null=True)
    city = models.CharField(max_length=50, verbose_name='Город', help_text='Укажите свой город', blank=True, null=True)
    avatar = models.ImageField(upload_to='users/avatar', blank=True, null=True, verbose_name='Аватар',
                               help_text='Загрузите аватар')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email


class Payments(models.Model):
    PAYMENT_METHOD = [
        ('Наличные', 'Наличные'),
        ('Перевод на счет', 'Перевод на счет')
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь',
                             help_text='Выберите пользователя')
    payment_date = models.DateField(verbose_name='дата оплаты', help_text='Укажите дату оплаты')
    payment_course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Оплаченный курс')
    payment_lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name='Оплаченный урок')
    payment_amount = models.PositiveIntegerField(verbose_name='Оплата', help_text='Введите сумму оплаты')
    payment_method = models.CharField(max_length=50, choices=PAYMENT_METHOD, verbose_name='Способ оплаты',
                                      help_text='Выберите способ оплаты')


class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь',
                             help_text='Укажите пользователя')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Курс',  help_text='Выберите курс')