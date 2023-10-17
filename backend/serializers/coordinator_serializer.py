from rest_framework import serializers
from backend.models.coordinator import Coordinator
from backend.models.permission import Permission
from backend.serializers.user_serializer import UserSerializer


class CoordinatorSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = UserSerializer.create(self, validated_data=user_data)

        permissions = Permission.objects.filter(id__in=[1, 2, 3, 4, 5, 6])
        user.permissions.add(*permissions)  # Permissão de leitura e escrita para todos os recursos

        return Coordinator.objects.create(user=user, **validated_data)

    class Meta:
        model = Coordinator
        fields = ["id", "user", "created"]
