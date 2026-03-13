import requests
from config import settings


def send_telegram_message(text, chat_id):
    params = {
        'text': text,
        'chat_id': chat_id,
    }
    response = requests.get(f'{settings.TELEGRAM_URL}{settings.BOT_TOKEN}/sendMessage', params=params)

    if response.status_code != 200:
        print(f"Ошибка отправки сообщения: {response.text}")
