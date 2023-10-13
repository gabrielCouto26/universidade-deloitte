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

    def create_user_profile(self):
        if self.user_type == User.UserType.STUDENT:
            Student.objects.create(user=self)
        elif self.user_type == User.UserType.TEACHER:
            Teacher.objects.create(user=self)
        elif self.user_type == User.UserType.COORDINATOR:
            Coordinator.objects.create(user=self)


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

