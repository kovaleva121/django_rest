from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название курса', help_text='Введите название курса')
    preview = models.ImageField(upload_to='materials/preview/course', blank=True, null=True,
                                verbose_name='Превью курса',
                                help_text='Загрузите превью курса')
    description = models.TextField(blank=True, null=True, verbose_name='Описание курса',
                                   help_text='Введите описание курса')

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'

    def __str__(self):
        return self.title


class Lesson(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название урока', help_text='Введите название урока')
    description = models.TextField(blank=True, null=True, verbose_name='Описание урока',
                                   help_text='Введите описание урока')
    preview = models.ImageField(upload_to='materials/preview/course/lesson', blank=True, null=True,
                                verbose_name='Превью урока',
                                help_text='Загрузите превью урока')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Курс', help_text='Выберите курс')
    link = models.URLField(blank=True, null=True, verbose_name='Ссылка', help_text='Прикрепите ссылку')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
