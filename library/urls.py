"""library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import #the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from authentication import views
from book import views as v

# from order import views as order_views
# from author import urls,views as view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home_guest/', views.home_guest_view, name='home_guest'),
    path('home_librarian/', views.home_librarian_view, name='home_librarian'),
    path('register/', views.register, name='register'),
    path('', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('book/', v.book_list, name='book_list'),
    path('api/v1/', include('author.urls'),name='api'),
    path('api/v1/', include('order.urls'), name='order_list'),
    path('', include('book.urls')),
    path('', include('authentication.urls')),
    # path('api/v1/orders/{id}', include('author.urls'), name='api_orders'),
    # path('', include('order.urls'), name='api2'),
]
