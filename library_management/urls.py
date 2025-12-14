from django.contrib import admin
from django.urls import path
from django.urls import include
from rest_framework.urls import app_name

from .apps import LibraryManagementConfig
from library_management.views import BookCreateApiView, BookListApiView

app_name = LibraryManagementConfig.name

urlpatterns = [
    path("book_create/", BookCreateApiView.as_view(), name="book_create"),
    path("book_list/", BookListApiView.as_view(), name="book_list"),
]