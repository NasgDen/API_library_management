from django.contrib import admin
from django.urls import path
from django.urls import include

from .apps import UsersConfig
from .views import UserCreateApiView, UserListApiView, UserRetrieveApiView, UserUpdateApiView, UserDestroyApiView

app_name = UsersConfig.name

urlpatterns = [
    path("user_create/", UserCreateApiView.as_view(), name="user_create"),
    path("user_list/", UserListApiView.as_view(), name="user_list"),
    path("user_retrieve/<int:pk>/", UserRetrieveApiView.as_view(), name="user_retrieve"),
    path("user_update/<int:pk>/", UserUpdateApiView.as_view(), name="user_update"),
    path("user_delete/<int:pk>/", UserDestroyApiView.as_view(), name="user_delete"),
]