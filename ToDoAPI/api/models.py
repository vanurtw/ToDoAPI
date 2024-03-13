from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.


class Task(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Задача')
    completed = models.BooleanField(default=False, verbose_name='Выполнена')
    data_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    data_update = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    author = models.ForeignKey(get_user_model(), verbose_name='Пользователь', on_delete=models.CASCADE)

    class Meta:
        ordering = ['data_create']
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
