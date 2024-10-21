from django import forms
from django.contrib.auth.forms import AuthenticationForm

from .models import CustomUser


class CustomAuthenticationForm(AuthenticationForm):
    email = forms.EmailField(required=True, label='Email')
    password = forms.CharField(widget=forms.PasswordInput, required=True, label='Password')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields.pop('username')


class CustomUserCreationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    role = forms.ChoiceField(choices=[(0, 'Visitor'), (1, 'Librarian')], required=True)

    class Meta:
        model = CustomUser
        fields = ['email', 'password', 'role']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])  # Hash the password
        if commit:
            user.save()
        return user
