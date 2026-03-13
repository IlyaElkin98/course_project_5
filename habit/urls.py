from django.urls import path, include
from rest_framework.routers import DefaultRouter

from habit.apps import HabitConfig
from habit.views import HabitViewSet

router = DefaultRouter()
router.register(r'habit', HabitViewSet, basename='habit')


app_name = HabitConfig.name

urlpatterns = [
    path('', include(router.urls)),
] + router.urls
