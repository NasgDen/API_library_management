from rest_framework.permissions import BasePermission


class IsLibrarian(BasePermission):
    """Класс реализует проверку разрешений для группы - Библиотекарь"""

    def has_permission(self, request, view):
        if request.user.groups.filter(name="librarian").exists():
            return True
        return False


class IsOwner(BasePermission):
    """Класс реализует проверку разрешений - создатель контента"""

    def has_object_permission(self, request, view, obj):
        return request.user == obj.owner
