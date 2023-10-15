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
    auth_user = models.ForeignKey(
        'auth.User',
        related_name='user',
        on_delete=models.SET_NULL,
        blank=True,
        null=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']
