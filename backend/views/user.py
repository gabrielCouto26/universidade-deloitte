from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from backend.models.user import User
from backend.serializers.user_serializer import UserSerializer


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserInfoView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, *args, **kwargs):
        user = User.objects.get(email=request.user.username)
        user_data = {
            'id': user.id,
            'email': user.email,
            'name': user.name,
            'birthday': user.birthday,
            'user_type': user.get_user_type_display(),
            'permissions': [],
        }

        for permission in user.permissions.all():
            user_data['permissions'].append({
                'resource': permission.get_resource_display(),
                'can_read': permission.can_read,
                'can_write': permission.can_write,
            })

        return Response(user_data)
