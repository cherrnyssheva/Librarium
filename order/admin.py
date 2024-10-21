from django.contrib import admin
from .models import Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'book', 'book_id', 'created_at', 'end_at']
    search_fields = ['user__email', 'book__name']
    list_filter = ['created_at']
    ordering = ['created_at']

    # Method to display book_id
    def book_id(self, obj):
        return obj.book.id

    book_id.short_description = 'Book ID'  # Title to display in the admin panel