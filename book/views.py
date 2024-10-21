from django.shortcuts import render
from rest_framework import viewsets
from .forms import BookFilterForm
from .models import Book
from .serializers import BookSerializer

def book_list(request):
    form = BookFilterForm(request.GET or None)
    books = Book.objects.all()

    sort_by = request.GET.get('sort_by')

    if sort_by == 'name':
        books = books.order_by('name')
    elif sort_by == 'count':
        books = books.order_by('count')
    elif sort_by == 'author':
        books = books.order_by('authors__name')

    return render(request, 'book.html', {'form': form, 'books': books})

class BookView(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer