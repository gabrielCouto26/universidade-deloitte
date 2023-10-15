from rest_framework import serializers
from backend.models.student import Student
from backend.models.discipline import Discipline
from backend.models.grade import Grade


class GradeSerializer(serializers.ModelSerializer):
    student = serializers.PrimaryKeyRelatedField(queryset=Student.objects.all())
    discipline = serializers.PrimaryKeyRelatedField(queryset=Discipline.objects.all())

    class Meta:
        model = Grade
        fields = ["id", "value", "student", "discipline"]
