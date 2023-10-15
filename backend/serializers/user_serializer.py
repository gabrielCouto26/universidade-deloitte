from rest_framework import serializers
from backend.models.user import User
from django.contrib.auth.models import User as AuthUser


class UserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        auth_data = {
            "username": validated_data.get('email'),
            "password": "admin"
        }
        validated_data['auth_user'] = AuthUser.objects.create_user(**auth_data)
        return User.objects.create(**validated_data)

    class Meta:
        model = User
        fields = ["id", "user_type", "email", "name", "birthday", "created"]
