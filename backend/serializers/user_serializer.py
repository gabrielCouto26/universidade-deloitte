from rest_framework import serializers
from backend.models.user import User
from backend.serializers.permission_serializer import PermissionSerializer
from django.contrib.auth.models import User as AuthUser


class UserSerializer(serializers.ModelSerializer):
    permissions = serializers.PrimaryKeyRelatedField(
        many=True,
        read_only=True)

    def create(self, validated_data):
        auth_data = {
            "username": validated_data.get('email'),
            "password": "admin"
        }
        validated_data['auth_user'] = AuthUser.objects.create_user(**auth_data)
        return User.objects.create(**validated_data)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['permissions'] = PermissionSerializer(instance.permissions.all(), many=True).data
        return data

    class Meta:
        model = User
        fields = ["id", "user_type", "email", "name", "birthday", "permissions", "created"]
