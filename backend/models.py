from django.db import models


class User(models.Model):
    class UserType(models.IntegerChoices):
        STUDENT = 1
        TEACHER = 2
        COORDINATOR = 3

    user_type = models.IntegerField(
        choices=UserType.choices,
        default=UserType.STUDENT)

    email = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=50)
    birthday = models.DateField()


class Coordinator(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE)
    

class Teacher(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE)
    

class Student(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE)
    

class Discipline(models.Model):
    name = models.CharField(max_length=30)
    workload = models.IntegerField()
    teacher = models.ForeignKey(
        Teacher,
        on_delete=models.SET_NULL,
        blank=True,
        null=True)
    students = models.ManyToManyField(
        Student,
        related_name='disciplines')

