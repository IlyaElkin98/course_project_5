from rest_framework.serializers import ModelSerializer

from habit.models import Habit
from habit.validators import HabitValidate


class HabitSerializer(ModelSerializer):
    """Сериализатор для привычки"""

    class Meta:
        model = Habit
        fields = '__all__'
        ordering_fields = ('id',)
        validators = [HabitValidate(), ]
