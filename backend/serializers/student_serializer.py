from rest_framework import serializers
from backend.models.student import Student
from backend.serializers.user_serializer import UserSerializer


class StudentSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Student
        fields = ["id", "user", "created"]
