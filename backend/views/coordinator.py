from rest_framework import generics
from backend.models.coordinator import Coordinator
from backend.serializers.coordinator_serializer import CoordinatorSerializer


class CoordinatorList(generics.ListCreateAPIView):
    queryset = Coordinator.objects.all()
    serializer_class = CoordinatorSerializer


class CoordinatorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Coordinator.objects.all()
    serializer_class = CoordinatorSerializer
