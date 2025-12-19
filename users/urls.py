from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .apps import UsersConfig
from .views import UserCreateApiView, UserDestroyApiView, UserListApiView, UserRetrieveApiView, UserUpdateApiView

app_name = UsersConfig.name

urlpatterns = [
    path("user_create/", UserCreateApiView.as_view(), name="user_create"),
    path("user_list/", UserListApiView.as_view(), name="user_list"),
    path("user_retrieve/<int:pk>/", UserRetrieveApiView.as_view(), name="user_retrieve"),
    path("user_update/<int:pk>/", UserUpdateApiView.as_view(), name="user_update"),
    path("user_delete/<int:pk>/", UserDestroyApiView.as_view(), name="user_delete"),
    path("login/", TokenObtainPairView.as_view(), name="login"),
    path("token_refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
