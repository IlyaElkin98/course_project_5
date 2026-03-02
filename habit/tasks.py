from time import strptime

from habit.models import Habit
from habit.service import send_telegram_message
from users.models import User
from celery import shared_task
from datetime import datetime, timedelta


@shared_task
def reminder_time():
    """Задача, отправка уведомления в телеграм"""
    reminders = Habit.objects.all()
    current_time = datetime.now().time()  # Получаем текущее время
    for reminder in reminders:
        reminder_time = reminder.time
        if reminder.user.tg_chat_id and reminder_time.hour == current_time.hour and reminder_time.minute == current_time.minute:
            message = f"Время для {reminder.action} в {reminder.time} в {reminder.location}"
            send_telegram_message(message, reminder.user.tg_chat_id)


