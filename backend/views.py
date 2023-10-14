from rest_framework import generics
from backend.models import User, Student, Teacher, Coordinator, Discipline
from backend.serializers import (
    UserSerializer,
    StudentSerializer,
    TeacherSerializer,
    CoordinatorSerializer,
    DisciplineSerializer
)


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
