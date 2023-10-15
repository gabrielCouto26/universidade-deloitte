from rest_framework import serializers
from backend.models.student import Student
from backend.models.discipline import Discipline


class GradeSerializer(serializers.ModelSerializer):
    student = serializers.PrimaryKeyRelatedField(queryset=Student.objects.all())
    discipline = serializers.PrimaryKeyRelatedField(queryset=Discipline.objects.all())

    class Meta:
        model = Discipline
        fields = ["id", "value", "student", "discipline"]
