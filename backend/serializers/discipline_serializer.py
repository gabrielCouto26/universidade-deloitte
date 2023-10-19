from rest_framework import serializers
from backend.models.discipline import Discipline
from backend.serializers.student_serializer import StudentSerializer


class DisciplineSerializer(serializers.ModelSerializer):
    teacher = serializers.SerializerMethodField()
    students = serializers.SerializerMethodField()
    grades = serializers.ReadOnlyField(source='get_grade')

    def get_teacher(self, obj):
        return obj.teacher.user.name if obj.teacher and obj.teacher.user else None

    def get_students(self, obj):
        """
        Retorna lista de STUDENTS se a requisição for de detalhes.
        Retorna contagem de STUDENTS se a requisição for de listagem.
        """
        if ("request" in self.context and
                self.context["request"].resolver_match.url_name == "discipline"):

            students = obj.students.all()
            student_serializer = StudentSerializer(students, many=True)
            return student_serializer.data
        else:
            return obj.students.count()

    class Meta:
        model = Discipline
        fields = ["id", "name", "workload", "teacher", "students", "grades", "created"]
