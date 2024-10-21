from django import forms


class AuthorFilterForm(forms.Form):
    name = forms.CharField(required=False, label='Name')
    book_count = forms.IntegerField(required=False, label='Minimum Books')


class AuthorSearchForm(forms.Form):
    search_name = forms.CharField(required=False, label='Search by Name')
