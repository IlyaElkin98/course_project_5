from django.contrib import admin

from users.models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'email', 'phone', 'city', 'tg_chat_id']
    list_filter = ('id',)
    search_fields = ("email",)
