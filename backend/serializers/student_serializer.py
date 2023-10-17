from rest_framework import serializers
from backend.models.student import Student
from backend.models.permission import Permission
from backend.serializers.user_serializer import UserSerializer


class StudentSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = UserSerializer.create(self, validated_data=user_data)

        permission = Permission.objects.get(id=17)
        user.permissions.add(permission)  # Permissão apenas para leitura de GRADE

        return Student.objects.create(user=user, **validated_data)

    class Meta:
        model = Student
        fields = ["id", "user", "created"]
