from rest_framework import serializers
from backend.models.teacher import Teacher
from backend.serializers.user_serializer import UserSerializer


class TeacherSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Teacher
        fields = ["id", "user", "created"]
