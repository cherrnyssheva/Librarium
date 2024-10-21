from django.urls import path
from .views import author_list

urlpatterns = [
    path('authors/{id}/', author_list, name='author_list'),
]