from rest_framework import viewsets

from habit.models import Habit
from habit.paginations import CustomPagination
from habit.serializers import HabitSerializer
from users.permissions import IsOwner


class HabitViewSet(viewsets.ModelViewSet):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    pagination_class = CustomPagination

    def get_permissions(self):
        """Определяем права доступа с учетом запрашиваемого действия"""
        if self.action == 'create':
            self.permission_classes = [~IsOwner]
        elif self.action in ['list', 'retrieve', 'update']:
            self.permission_classes = [IsOwner]
        elif self.action == 'destroy':
            self.permission_classes = [IsOwner]
        return [permission() for permission in self.permission_classes]

    def perform_create(self, serializer):
        """Привязываем текущего пользователя к создаваемому объекту"""
        new_habit = serializer.save()
        new_habit.is_owner = self.request.user
        new_habit.save()

    def get_queryset(self):
        """Фильтруем данные в зависимости от прав доступа"""
        if self.request.user.is_authenticated:
            # Если у пользователя есть привычки, вернуть только их
            return self.queryset.filter(user=self.request.user)  # Либо другие условия
        return self.queryset.none()