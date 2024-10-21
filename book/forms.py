from django import forms


class BookFilterForm(forms.Form):
    sort_by = forms.ChoiceField(
        choices=[
            ('', 'Select'),
            ('name', 'Name'),
            ('count', 'Count'),
            ('author', 'Author')
        ],
        required=False,
        label='Sort by'
    )
