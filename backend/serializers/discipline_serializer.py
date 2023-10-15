from rest_framework import serializers
from backend.models.discipline import Discipline
from backend.models.teacher import Teacher
from backend.models.student import Student
from backend.serializers.teacher_serializer import TeacherSerializer
from backend.serializers.student_serializer import StudentSerializer


class DisciplineSerializer(serializers.ModelSerializer):
    teacher = serializers.PrimaryKeyRelatedField(queryset=Teacher.objects.all())
    students = serializers.PrimaryKeyRelatedField(many=True, queryset=Student.objects.all())
    grades = serializers.ReadOnlyField(source='get_grade')

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['teacher'] = TeacherSerializer(instance.teacher).data
        data['students'] = [
            StudentSerializer(student).data for student in instance.students.all()]
        return data

    class Meta:
        model = Discipline
        fields = ["id", "name", "workload", "teacher", "students", "grades", "created"]
