from rest_framework import serializers
from backend.models import Student, Discipline


class GradeSerializer(serializers.ModelSerializer):
    student = serializers.PrimaryKeyRelatedField(queryset=Student.objects.all())
    disciplin = serializers.PrimaryKeyRelatedField(queryset=Discipline.objects.all())

    class Meta:
        model = Discipline
        fields = ["id", "value", "student", "discipline"]
