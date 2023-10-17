from django.db import models


class Permission(models.Model):
    RESOURCE_CHOICES = [
        (1, 'User'),
        (2, 'Student'),
        (3, 'Teacher'),
        (4, 'Coordinator'),
        (5, 'Discipline'),
        (6, 'Grade'),
    ]

    resource = models.CharField(max_length=20, choices=RESOURCE_CHOICES)
    can_read = models.BooleanField(default=False)
    can_write = models.BooleanField(default=False)

    class Meta:
        ordering = ['resource']
        unique_together = ('resource', 'can_read', 'can_write')
