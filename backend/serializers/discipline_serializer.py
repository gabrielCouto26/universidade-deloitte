from rest_framework import serializers
from backend.models.discipline import Discipline


class DisciplineSerializer(serializers.ModelSerializer):
    teacher = serializers.SerializerMethodField()
    students = serializers.SerializerMethodField()
    grades = serializers.ReadOnlyField(source='get_grade')

    def get_teacher(self, obj):
        return obj.teacher.user.name if obj.teacher and obj.teacher.user else None

    def get_students(self, obj):
        return obj.students.count()

    class Meta:
        model = Discipline
        fields = ["id", "name", "workload", "teacher", "students", "grades", "created"]
