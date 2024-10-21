from django.contrib import admin
from .models import Author

#
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
     list_display = ['surname','name', 'patronymic', 'books_count']
     search_fields = ['surname', 'books']
     list_filter = ['surname']
     ordering = ['surname']

     def books_count(self, obj):
          return obj.books.count() # Returns the number of related books

     books_count.short_description = 'Number of Books' # Title to display in the admin panel
