from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    """Проверяет, является ли пользователь владельцем."""

    def has_object_permission(self, request, view, obj):
        return request.user.is_superuser or obj.user.id == request.user.id