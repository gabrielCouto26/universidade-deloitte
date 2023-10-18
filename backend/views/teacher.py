from rest_framework import generics
from backend.models.teacher import Teacher
from backend.models.user import User
from backend.models.grade import Grade
from backend.models.discipline import Discipline
from backend.serializers.teacher_serializer import TeacherSerializer
from backend.serializers.grade_serializer import GradeSerializer
from backend.serializers.discipline_serializer import DisciplineSerializer
from backend.permissions import IsTeacher, CanList


class TeacherList(generics.ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class TeacherDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


# Teacher Grades
class TeacherGradeList(generics.ListCreateAPIView):
    serializer_class = GradeSerializer
    permission_classes = [IsTeacher, CanList]

    def get_queryset(self):
        user = User.objects.get(email=self.request.user.username)
        return Grade.objects.filter(
            discipline__teacher__user=user)


# Teacher Disciplines
class TeacherDisciplineList(generics.ListCreateAPIView):
    queryset = Discipline.objects.all()
    serializer_class = DisciplineSerializer
    permission_classes = [IsTeacher, CanList]

    def get_queryset(self):
        user = User.objects.get(email=self.request.user.username)
        return Discipline.objects.filter(
            teacher__user=user)
