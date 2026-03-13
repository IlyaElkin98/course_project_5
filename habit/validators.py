from rest_framework.exceptions import ValidationError


class HabitValidate:
    """Проверка правильности заполнения полей привычки"""
    """Для сериализатора"""
    def __init__(
            self,
            is_pleasant='is_pleasant',
            related_habit='related_habit',
            period='period',
            reward='reward',
            duration='duration',
    ):
        self.is_pleasant = is_pleasant
        self.related_habit = related_habit
        self.period = period
        self.reward = reward
        self.duration = duration

    def __call__(self, attrs):
        if attrs.get(self.related_habit) is not None and attrs.get(self.reward) is not None:
            message = 'Нельзя выбрать одновременно и связанную привычку и вознаграждение'
            raise ValidationError(message)

        if attrs.get(self.related_habit) and not attrs[self.related_habit].is_pleasant:
            message = 'Связанной привычкой можно назначить только приятную привычку'
            raise ValidationError(message)

        if attrs[self.duration] > 120:
            message = 'Время выполнения привычки должно быть меньше 2 минут (120 секунд)'
            raise ValidationError(message)

        if attrs.get(self.is_pleasant) and (attrs.get(self.reward) or attrs.get(self.related_habit)):
            message = 'У приятной привычки не может быть вознаграждения или связанной привычки'
            raise ValidationError(message)

        if attrs.get(self.period):
            if attrs[self.period] > 7:
                message = 'Период выполнения привычки должен быть меньше 7 дней'
                raise ValidationError(message)
