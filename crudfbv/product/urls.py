from django.contrib import admin
from django.urls import path, include
from .views import ProductsListView, ProductAddView, ProductUpdateView, ProductDeleteView
from book.views import create_view, view_books_list, delete_book, update_book

urlpatterns = [
    path('', ProductsListView.as_view(), name='viewproducturlname'),
    path('addproduct/', ProductAddView.as_view(), name='addproducturlname'),
    path('update/<int:id>', ProductUpdateView.as_view(), name='updateproducturlname'),
    path('delete/<int:id>', ProductDeleteView.as_view(), name='deleteproducturlname')
]
