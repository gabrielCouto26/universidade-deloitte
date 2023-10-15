from rest_framework import serializers
from backend.models.discipline import Discipline
from backend.serializers.teacher_serializer import TeacherSerializer
from backend.serializers.student_serializer import StudentSerializer
from backend.serializers.grade__serializer import GradeSerializer


class DisciplineSerializer(serializers.ModelSerializer):
    teacher = TeacherSerializer()
    students = StudentSerializer(many=True)
    grades = GradeSerializer(many=True)

    class Meta:
        model = Discipline
        fields = ["id", "name", "workload", "teacher", "students", "grades", "created"]
