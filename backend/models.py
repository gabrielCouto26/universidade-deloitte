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
