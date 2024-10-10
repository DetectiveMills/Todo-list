from django.db import models

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length = 155, verbose_name = 'Заголовок задачи')
    description = models.TextField(verbose_name = 'Описание задачи')
    completed = models.BooleanField(default = False, verbose_name = 'Статус выполнения')
    created = models.DateTimeField(auto_now_add = True, verbose_name = 'Время')

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'Todo list'
        verbose_name_plural = 'Todo list'

