from rest_framework import generics
from backend.models.discipline import Discipline
from backend.serializers.discipline_serializer import DisciplineSerializer
from backend.permissions import IsCoordinator, IsTeacher, CanList


class DisciplineList(generics.ListCreateAPIView):
    permission_classes = [IsCoordinator | IsTeacher, CanList]
    queryset = Discipline.objects.all()
    serializer_class = DisciplineSerializer


class DisciplineDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Discipline.objects.all()
    serializer_class = DisciplineSerializer
