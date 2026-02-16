from django.db import models

class Habit(models.Model):
    ACTION_CHOICES = [
        ('полезная', 'Полезная'),
        ('приятная', 'Приятная'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='habit', verbose_name='Пользователь')
    location = models.CharField(max_length=100, verbose_name='Локация выполнения привычки')
    time = models.TimeField()
    action = models.CharField(max_length=100, verbose_name='Действие')
    is_pleasant = models.BooleanField(default=False, verbose_name='Признак приятности привычки')
    related_habit = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL,
                                      related_name='related_habits', verbose_name='Связанная привычка ')
    period = models.PositiveIntegerField(default=1, verbose_name='Периодичность выполнения привычки')
    reward = models.CharField(max_length=150, verbose_name='Вознаграждение')
    duration = models.PositiveIntegerField(verbose_name='Продолжительность выполнения привычки')
    is_public = models.BooleanField(default=False, verbose_name='Признак публичности')

    def __str__(self):
        return f'{self.action} в {self.time} в {self.location}'

    class Meta:
        verbose_name = "Привычка"
        verbose_name_plural = "Привычки"



