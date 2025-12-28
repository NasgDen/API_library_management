from rest_framework.permissions import BasePermission


class IsUser(BasePermission):
    """Зарегистрированный пользователь может изменять только свой профиль"""

    def has_object_permission(self, request, view, obj):
        return request.user == obj
