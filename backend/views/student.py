from rest_framework import generics
from backend.models.student import Student
from backend.models.user import User
from backend.models.grade import Grade
from backend.serializers.student_serializer import StudentSerializer
from backend.serializers.grade_serializer import GradeSerializer
from backend.permissions import (
    IsCoordinator,
    IsTeacher,
    IsStudent,
    CanList)


class StudentList(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsCoordinator | IsTeacher, CanList]


class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


# Student Grades
class StudentGradeList(generics.ListCreateAPIView):
    serializer_class = GradeSerializer
    permission_classes = [IsStudent, CanList]

    def get_queryset(self):
        user = User.objects.get(email=self.request.user.username)
        return Grade.objects.filter(student__user=user)
