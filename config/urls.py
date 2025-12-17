from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("library_management.urls", namespace="library_management")),
    path("users/", include("users.urls", namespace="users")),
]
