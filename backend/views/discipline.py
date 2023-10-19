from rest_framework import generics, status
from rest_framework.response import Response
from backend.models.discipline import Discipline
from backend.models.teacher import Teacher
from backend.models.student import Student
from backend.serializers.discipline_serializer import DisciplineSerializer
from backend.serializers.student_serializer import StudentSerializer
from backend.permissions import IsCoordinator, IsTeacher, CanList


class DisciplineList(generics.ListCreateAPIView):
    permission_classes = [IsCoordinator | IsTeacher]
    queryset = Discipline.objects.all()
    serializer_class = DisciplineSerializer

    def create(self, request, *args, **kwargs):
        data = request.data

        teacher_id = data.get('teacher')
        student_ids = data.get('students', [])

        teacher = Teacher.objects.get(id=teacher_id)

        students = []
        for student_id in student_ids:
            student = Student.objects.get(id=student_id)
            students.append(student)

        discipline = Discipline.objects.create(
            teacher=teacher,
            name=data['name'],
            workload=data['workload'])

        discipline.students.set(students)

        serializer = DisciplineSerializer(discipline)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class DisciplineDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Discipline.objects.all()
    serializer_class = DisciplineSerializer


class DisciplineStudentList(generics.ListAPIView):
    serializer_class = StudentSerializer
    permission_classes = [IsTeacher, CanList]

    def get_queryset(self):
        discipline_id = self.kwargs.get('pk')
        discipline = Discipline.objects.get(pk=discipline_id)

        return discipline.students.all()
