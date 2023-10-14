from rest_framework import serializers
from backend.models import User, Teacher


class TeacherSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Teacher
        fields = ["id", "user", "disciplines", "created"]
