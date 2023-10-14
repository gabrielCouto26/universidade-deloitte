from rest_framework import serializers
from .models import User, Student, Teacher, Coordinator, Discipline


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "user_type", "email", "name", "birthday", "created"]


class StudentSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Student
        fields = ["id", "user", "disciplines", "grades", "created"]


class TeacherSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Teacher
        fields = ["id", "user", "disciplines", "created"]


class CoordinatorSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Coordinator
        fields = ["id", "user", "created"]


class DisciplineSerializer(serializers.ModelSerializer):
    teacher = serializers.PrimaryKeyRelatedField(queryset=Teacher.objects.all())
    students = serializers.PrimaryKeyRelatedField(many=True, queryset=Student.objects.all())

    class Meta:
        model = Discipline
        fields = ["id", "name", "workload", "teacher", "students", "grades", "created"]


class GradeSerializer(serializers.ModelSerializer):
    student = serializers.PrimaryKeyRelatedField(queryset=Student.objects.all())
    disciplin = serializers.PrimaryKeyRelatedField(queryset=Discipline.objects.all())

    class Meta:
        model = Discipline
        fields = ["id", "value", "student", "discipline"]
