from rest_framework import serializers
from backend.models.student import Student
from backend.models.teacher import Teacher
from backend.models.discipline import Discipline


class DisciplineSerializer(serializers.ModelSerializer):
    teacher = serializers.PrimaryKeyRelatedField(queryset=Teacher.objects.all())
    students = serializers.PrimaryKeyRelatedField(many=True, queryset=Student.objects.all())

    class Meta:
        model = Discipline
        fields = ["id", "name", "workload", "teacher", "students", "grades", "created"]
