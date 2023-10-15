from rest_framework import serializers
from backend.models.student import Student
from backend.models.discipline import Discipline
from backend.models.grade import Grade
from backend.serializers.student_serializer import StudentSerializer
from backend.serializers.discipline_serializer import DisciplineSerializer


class GradeSerializer(serializers.ModelSerializer):
    student = serializers.PrimaryKeyRelatedField(queryset=Student.objects.all())
    discipline = serializers.PrimaryKeyRelatedField(queryset=Discipline.objects.all())

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['student'] = StudentSerializer(
            instance.student).data.get('user').get('name')
        data['discipline'] = DisciplineSerializer(
            instance.discipline).data.get('name')
        return data

    class Meta:
        model = Grade
        fields = ["id", "value", "student", "discipline"]
