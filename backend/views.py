from rest_framework import generics
from backend.models.user import User
from backend.models.student import Student
from backend.models.teacher import Teacher
from backend.models.coordinator import Coordinator
from backend.models.discipline import Discipline
from backend.models.grade import Grade
from backend.serializers.user_serializer import UserSerializer
from backend.serializers.student_serializer import StudentSerializer
from backend.serializers.teacher_serializer import TeacherSerializer
from backend.serializers.coordinator_serializer import CoordinatorSerializer
from backend.serializers.discipline_serializer import DisciplineSerializer
from backend.serializers.grade_serializer import GradeSerializer
from backend.permissions import (
    IsStudent,
    IsTeacher,
    IsCoordinator,
    CanList,
    CanShowGrade)


# User
class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# Student
class StudentList(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


# Teacher
class TeacherList(generics.ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class TeacherDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


# Coordinator
class CoordinatorList(generics.ListCreateAPIView):
    queryset = Coordinator.objects.all()
    serializer_class = CoordinatorSerializer


class CoordinatorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Coordinator.objects.all()
    serializer_class = CoordinatorSerializer


# Discipline
class DisciplineList(generics.ListCreateAPIView):
    queryset = Discipline.objects.all()
    serializer_class = DisciplineSerializer


class DisciplineDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Discipline.objects.all()
    serializer_class = DisciplineSerializer


# Grade
class GradeList(generics.ListCreateAPIView):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer
    permission_classes = [IsCoordinator, CanList]


class GradeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer
    permission_classes = [IsStudent | IsTeacher, CanShowGrade]


# Student Grades
class StudentGradeList(generics.ListCreateAPIView):
    serializer_class = GradeSerializer
    permission_classes = [IsStudent, CanList]

    def get_queryset(self):
        user = User.objects.get(email=self.request.user.username)
        return Grade.objects.filter(student__user=user)


# Teacher Grades
class TeacherGradeList(generics.ListCreateAPIView):
    serializer_class = GradeSerializer
    permission_classes = [IsTeacher, CanList]

    def get_queryset(self):
        user = User.objects.get(email=self.request.user.username)
        return Grade.objects.filter(
            discipline__teacher__user=user)
