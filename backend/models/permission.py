from django.db import models


class Permission(models.Model):
    RESOURCE_CHOICES = [
        ('USER', 'User'),
        ('STUDENT', 'Student'),
        ('TEACHER', 'Teacher'),
        ('COORDINATOR', 'Coordinator'),
        ('DISCIPLINE', 'Discipline'),
        ('GRADE', 'Grade'),
    ]

    resource = models.CharField(max_length=20, choices=RESOURCE_CHOICES)
    can_read = models.BooleanField(default=False)
    can_write = models.BooleanField(default=False)

    class Meta:
        ordering = ['resource']
        unique_together = ('resource', 'can_read', 'can_write')
