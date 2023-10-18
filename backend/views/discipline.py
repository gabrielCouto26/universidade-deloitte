from rest_framework import generics
from backend.models.discipline import Discipline
from backend.serializers.discipline_serializer import DisciplineSerializer
from backend.serializers.student_serializer import StudentSerializer
from backend.permissions import IsCoordinator, IsTeacher, CanList


class DisciplineList(generics.ListCreateAPIView):
    permission_classes = [IsCoordinator | IsTeacher, CanList]
    queryset = Discipline.objects.all()
    serializer_class = DisciplineSerializer


class DisciplineDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Discipline.objects.all()
    serializer_class = DisciplineSerializer


class DisciplineStudentList(generics.ListAPIView):
    serializer_class = StudentSerializer
    permission_classes = [IsTeacher, CanList]

    def get_queryset(self):
        discipline_id = self.kwargs.get('pk')
        discipline = Discipline.objects.get(pk=discipline_id)

        return discipline.students.all()
