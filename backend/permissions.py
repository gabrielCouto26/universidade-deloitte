from rest_framework import permissions
from backend.models.user import User
from backend.models.grade import Grade


class IsCoordinator(permissions.BasePermission):
    def has_permission(self, request, view):

        # Verifica se usuário está autenticado
        if not request.user.is_authenticated:
            return False

        user = User.objects.get(email=request.user.username)

        # Verifica se usuário autenticado é COORDINATOR
        if not user.user_type == User.UserType.COORDINATOR:
            return False

        return True


class IsStudent(permissions.BasePermission):
    def has_permission(self, request, view):

        # Verifica se usuário está autenticado
        if not request.user.is_authenticated:
            return False

        # Verifica se usuário está apenas visualizando
        if request.method not in permissions.SAFE_METHODS:
            return False

        user = User.objects.get(email=request.user.username)

        # Verifica se usuário autenticado é STUDENT
        if not user.user_type == User.UserType.STUDENT:
            return False

        return True


class IsTeacher(permissions.BasePermission):
    def has_permission(self, request, view):

        # Verifica se usuário está autenticado
        if not request.user.is_authenticated:
            return False

        user = User.objects.get(email=request.user.username)

        # Verifica se usuário autenticado é TEACHER
        if not user.user_type == User.UserType.TEACHER:
            return False

        return True


class CanList(permissions.BasePermission):
    def has_permission(self, request, view):

        # Verifica se usuário está autenticado
        if not request.user.is_authenticated:
            return False

        # Verifica se usuário está apenas visualizando
        if request.method not in permissions.SAFE_METHODS:
            return False

        return True


class CanShowGrade(permissions.BasePermission):
    def has_permission(self, request, view):

        # Verifica se usuário está autenticado
        if not request.user.is_authenticated:
            return False

        # Verifica se usuário está apenas visualizando
        if request.method not in permissions.SAFE_METHODS:
            return False

        grade_id = view.kwargs.get('pk')

        user = User.objects.get(email=request.user.username)

        # Verifica se a GRADE buscada pertence às disciplinas do usuário que a busca
        if user.user_type == User.UserType.STUDENT:
            return Grade.objects.filter(
                student__user=user,
                pk=grade_id).exists()

        elif user.user_type == User.UserType.TEACHER:
            return Grade.objects.filter(
                discipline__teacher__user=user,
                pk=grade_id).exists()

        return False
