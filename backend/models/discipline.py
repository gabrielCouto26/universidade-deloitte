from django.db import models
from backend.models.teacher import Teacher
from backend.models.student import Student


class Discipline(models.Model):
    name = models.CharField(max_length=30)
    workload = models.IntegerField()
    teacher = models.ForeignKey(
        Teacher,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='disciplines')
    students = models.ManyToManyField(
        Student,
        related_name='disciplines')
    created = models.DateTimeField(auto_now_add=True)

    def get_grade(self):
        grades = []
        for g in self.grades.all():
            grades.append({
                "id": g.id,
                "value": g.value,
                "student": g.student.user.name,
            })
        return grades

    class Meta:
        ordering = ['created']
