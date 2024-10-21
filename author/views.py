from django.shortcuts import render
from .models import Author
from .forms import AuthorFilterForm, AuthorSearchForm

def author_list(request):
    filter_form = AuthorFilterForm(request.GET or None)
    search_form = AuthorSearchForm(request.GET or None)
    authors = Author.objects.all()
    if filter_form.is_valid():
        name = filter_form.cleaned_data.get('name')
        book_count = filter_form.cleaned_data.get('book_count')

        if name:
            authors = authors.filter(name__icontains=name)
        if book_count is not None:
            authors = authors.annotate(num_books=models.Count('books')).filter(num_books__gte=book_count)
    if search_form.is_valid():
        search_name = search_form.cleaned_data.get('search_name')
        if search_name:
            authors = authors.filter(name__icontains=search_name)

    return render(request, 'author.html', {
        'filter_form': filter_form,
        'search_form': search_form,
        'authors': authors
    })