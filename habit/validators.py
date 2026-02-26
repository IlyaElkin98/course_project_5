from django.core.exceptions import ValidationError
from .models import Habit


def validate_reward_or_related_habit(habit):
    if habit.reward and habit.related_habit:
        raise ValidationError("Нельзя одновременно указывать вознаграждение и связанную привычку.")


def validate_execution_time(time):
    if time > 120:
        raise ValidationError("Время выполнения не должно превышать 120 секунд.")


def validate_pleasant_habit(habit):
    if habit.is_pleasant:
        if habit.reward or habit.related_habit:
            raise ValidationError("У приятной привычки не может быть вознаграждения или связанной привычки.")


def validate_periodicity(period):
    if period < 1 or period > 7:
        raise ValidationError("Привычка должна выполняться хотя бы один раз в 7 дней.")


def validate_habit(habit):
    if habit.period > 7:
        raise ValidationError("Нельзя не выполнять привычку более 7 дней.")

