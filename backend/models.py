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
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']


class Student(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']


class Teacher(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']


class Coordinator(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']


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

    class Meta:
        ordering = ['created']


class Grade(models.Model):
    value = models.FloatField()
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name='grades')
    disciplines = models.ForeignKey(
        Discipline,
        on_delete=models.CASCADE,
        related_name='grades')
