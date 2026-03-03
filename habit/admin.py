from django.contrib import admin

from habit.models import Habit


@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    list_filter = ("id",)
    list_display = ['id', 'user', 'location', 'time', 'action', 'is_pleasant',
                    'related_habit', 'period', 'reward', 'duration', 'is_public', 'is_owner'
                    ]
    search_fields = ("action",)
