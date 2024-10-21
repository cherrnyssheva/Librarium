from django.contrib import admin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['email', 'first_name', 'last_name', 'is_active', 'is_staff']
    search_fields = ['email', 'first_name', 'last_name']
    list_filter = ['is_active', 'is_staff', 'role']
    ordering = ['email']