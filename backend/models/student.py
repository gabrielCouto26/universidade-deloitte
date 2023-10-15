from django.db import models
from backend.models.user import User


class Student(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']
