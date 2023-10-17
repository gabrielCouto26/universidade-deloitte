from rest_framework import serializers
from backend.models.teacher import Teacher
from backend.models.permission import Permission
from backend.serializers.user_serializer import UserSerializer


class TeacherSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = UserSerializer.create(self, validated_data=user_data)

        permission = Permission.objects.get(id=6)
        user.permissions.add(permission)  # Permissão para leitura e escrita de GRADE

        return Teacher.objects.create(user=user, **validated_data)

    class Meta:
        model = Teacher
        fields = ["id", "user", "created"]
