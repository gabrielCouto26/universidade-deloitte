from rest_framework import permissions
from backend.models.user import User


class IsCoordinator(permissions.BasePermission):
    def has_permission(self, request, view):
        user = User.objects.get(email=request.user.username)

        if user.user_type == User.UserType.COORDINATOR:
            return True

        return False


class IsStudent(permissions.BasePermission):
    def has_permission(self, request, view):
        user = User.objects.get(email=request.user.username)

        if request.method not in permissions.SAFE_METHODS:
            return False

        if user.user_type == User.UserType.STUDENT:
            return True

        return False


class IsTeacher(permissions.BasePermission):
    def has_permission(self, request, view):
        user = User.objects.get(email=request.user.username)

        if user.user_type == User.UserType.TEACHER:
            return True

        return False
