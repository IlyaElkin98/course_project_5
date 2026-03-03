from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from users.models import User
from habit.models import Habit


class HabitViewSetTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create(email='test@mail.ru')
        self.habit = Habit.objects.create(location="Улица", action="Прогулка",
                                          time="14:30:00", duration=10, user=self.user)
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_habit_retrieve(self):
        url = reverse('habit:habit-detail', args=(self.habit.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("action"), self.habit.action)

    def test_create_habit(self):
        url = reverse('habit:habit-list')
        data = {
            'user': self.user.id,
            'location': 'Yoga Studio',
            'time': '19:00:00',
            'action': 'Yoga',
            'is_pleasant': True,
            'duration': 30,
            "is_owner": self.user.id
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Habit.objects.count(), 2)

    def test_update_habit(self):
        data = {
            "location": "Park",
            "time": "10:00:00",
            "action": "Jogging",
            "duration": 90,
        }
        response = self.client.patch(reverse('habit:habit-detail', kwargs={'pk': self.habit.pk}), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.habit.refresh_from_db()
        self.assertEqual(self.habit.location, "Park")  # Проверяем, что привычка обновилась

    def test_delete_habit(self):
        response = self.client.delete(reverse('habit:habit-detail', kwargs={'pk': self.habit.pk}), format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Habit.objects.count(), 0)  # Проверка, что привычка удалена
