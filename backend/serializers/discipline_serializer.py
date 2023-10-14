from rest_framework import serializers
from backend.models import Student, Teacher, Discipline


class DisciplineSerializer(serializers.ModelSerializer):
    teacher = serializers.PrimaryKeyRelatedField(queryset=Teacher.objects.all())
    students = serializers.PrimaryKeyRelatedField(many=True, queryset=Student.objects.all())

    class Meta:
        model = Discipline
        fields = ["id", "name", "workload", "teacher", "students", "grades", "created"]
