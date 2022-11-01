"""crudfbv URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from book.views import create_view, view_books_list, delete_book, update_book

urlpatterns = [
    path('', create_view),
    path('viewlist/', view_books_list),
    path('delete/<int:id>', delete_book, name='delete_book'),
    path('update/<int:id>', update_book, name='update_book'),
    path('admin/', admin.site.urls),
]
