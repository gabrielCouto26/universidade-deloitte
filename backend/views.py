from rest_framework import viewsets
from rest_framework import permissions
from backend.models import UserType, User
from backend.serializers import UserTypeSerializer, UserSerializer


class UserTypeViewSet(viewsets.ModelViewSet):
    queryset = UserType.objects.all()
    serializer_class = UserTypeSerializer
    permission_classes = [permissions.IsAuthenticated]


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
