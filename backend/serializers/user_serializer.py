from rest_framework import serializers
from backend.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "user_type", "email", "name", "birthday", "created"]
