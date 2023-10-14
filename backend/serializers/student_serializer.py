from rest_framework import serializers
from backend.models import User, Student


class StudentSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Student
        fields = ["id", "user", "disciplines", "grades", "created"]
