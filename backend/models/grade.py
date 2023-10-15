from django.db import models
from backend.models.student import Student
from backend.models.discipline import Discipline


class Grade(models.Model):
    value = models.FloatField()
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name='grades')
    discipline = models.ForeignKey(
        Discipline,
        on_delete=models.CASCADE,
        related_name='grades')
