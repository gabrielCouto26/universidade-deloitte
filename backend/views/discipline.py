from rest_framework import generics
from backend.models.discipline import Discipline
from backend.serializers.discipline_serializer import DisciplineSerializer


class DisciplineList(generics.ListCreateAPIView):
    queryset = Discipline.objects.all()
    serializer_class = DisciplineSerializer


class DisciplineDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Discipline.objects.all()
    serializer_class = DisciplineSerializer
