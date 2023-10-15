from rest_framework import serializers
from backend.models.coordinator import Coordinator
from backend.serializers.user_serializer import UserSerializer


class CoordinatorSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = UserSerializer.create(self, validated_data=user_data)
        return Coordinator.objects.create(user=user, **validated_data)

    class Meta:
        model = Coordinator
        fields = ["id", "user", "created"]
