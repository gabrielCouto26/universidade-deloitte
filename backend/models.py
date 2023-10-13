from django.db import models


class UserType(models.Model):
    USER_TYPES = [
        (1, 'Student'),
        (2, 'Teacher'),
        (3, 'Coordinator'),
    ]

    type = models.IntegerField(
        choices=USER_TYPES,
        default=1
    )


class User(models.Model):
    user_type = models.ForeignKey(
        UserType,
        on_delete=models.SET_NULL,
        blank=True,
        null=True)
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

