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

    class Meta:
        db_table = 'user_types'

class User(models.Model):
    user_type = models.ForeignKey(
        UserType,
        on_delete=models.SET_NULL,
        blank=True,
        null=True)
    email = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=50)
    birthday = models.DateField()

    class Meta:
        db_table = 'users'
