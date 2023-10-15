from rest_framework import serializers
from backend.models.teacher import Teacher
from backend.serializers.user_serializer import UserSerializer


class TeacherSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = UserSerializer.create(self, validated_data=user_data)
        return Teacher.objects.create(user=user, **validated_data)

    class Meta:
        model = Teacher
        fields = ["id", "user", "created"]
