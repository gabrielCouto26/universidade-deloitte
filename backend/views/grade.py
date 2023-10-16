from rest_framework import generics
from backend.models.grade import Grade
from backend.serializers.grade_serializer import GradeSerializer
from backend.permissions import (
    IsStudent,
    IsTeacher,
    IsCoordinator,
    CanList,
    CanShowGrade)


class GradeList(generics.ListCreateAPIView):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer
    permission_classes = [IsCoordinator, CanList]


class GradeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer
    permission_classes = [IsStudent | IsTeacher, CanShowGrade]
