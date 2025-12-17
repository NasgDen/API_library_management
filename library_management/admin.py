from django.contrib import admin

from library_management.models import Author, Book, BookIssuance


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "year", "owner", "date_create", "date_update")
    list_filter = ("title",)
    search_fields = ("title",)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "patronymic", "owner", "date_create", "date_update")
    list_filter = ("last_name",)
    search_fields = ("last_name",)


@admin.register(BookIssuance)
class BookIssuanceAdmin(admin.ModelAdmin):
    list_display = (
        "book",
        "user",
        "book_issued",
        "book_returned",
        "owner",
        "date_create",
        "date_update",
        "date_return",
    )
    list_filter = (
        "book",
        "user",
    )
    search_fields = (
        "book",
        "user",
    )
