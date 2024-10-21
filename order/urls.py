from django.contrib import admin
from django.urls import path, include

from .views import order_list
urlpatterns = [
    path('order/{id}', order_list,name='order_list'),
]
