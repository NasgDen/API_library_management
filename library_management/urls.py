from django.contrib import admin
from django.urls import path
from django.urls import include
from rest_framework.urls import app_name

from .apps import LibraryManagementConfig
from library_management.views import BookCreateApiView, BookListApiView, AuthorCreateApiView, AuthorListApiView, \
    BookRetrieveAPIView, BookUpdateApiView, AuthorRetrieveApiView, AuthorUpdateApiView, BookDestroyApiView, \
    AuthorDestroyApiView, BookIssuanceCreateApiView

app_name = LibraryManagementConfig.name

urlpatterns = [
    path("book_create/", BookCreateApiView.as_view(), name="book_create"),
    path("book_list/", BookListApiView.as_view(), name="book_list"),
    path("book_retrieve/<int:pk>/", BookRetrieveAPIView.as_view(), name="book_retrieve"),
    path("book_update/<int:pk>/", BookUpdateApiView.as_view(), name="book_update"),
    path("book_delete/<int:pk>/", BookDestroyApiView.as_view(), name="book_delete"),
    path("author_create/", AuthorCreateApiView.as_view(), name="author_create"),
    path("author_list/", AuthorListApiView.as_view(), name="author_list"),
    path("author_retrieve/<int:pk>/", AuthorRetrieveApiView.as_view(), name="author_retrieve"),
    path("author_update/<int:pk>/", AuthorUpdateApiView.as_view(), name="author_update"),
    path("author_delete/<int:pk>/", AuthorDestroyApiView.as_view(), name="author_delete"),
    path("book_issuance_create/", BookIssuanceCreateApiView.as_view(), name="book_issuance_create"),
]