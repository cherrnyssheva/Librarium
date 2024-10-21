from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('books', views.BookView)

urlpatterns = [
    # path('all/', views.all_books, name='all_books'),
    path('api/v1/', include(router.urls))
]
