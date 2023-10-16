from django.shortcuts import redirect
from rest_framework import generics
from rest_framework.response import Response
from backend.models.user import User
from backend.permissions import (
    IsStudent,
    IsTeacher,
    IsCoordinator,
    CanList)


class HomeView(generics.ListCreateAPIView):
    permission_classes = [IsStudent | IsTeacher | IsCoordinator, CanList]

    def get(self, request, *args, **kwargs):
        user = User.objects.get(email=request.user.username)

        if user.user_type == User.UserType.STUDENT:
            return redirect('student-grades')
        elif user.user_type == User.UserType.TEACHER:
            return redirect('teacher-grades')
        elif user.user_type == User.UserType.COORDINATOR:
            return redirect('disciplines')
        else:
            return Response({'detail': 'Usuário não autorizado'}, status=403)
