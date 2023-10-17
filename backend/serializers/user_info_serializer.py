from rest_framework import serializers
from backend.serializers.permission_serializer import PermissionSerializer


class UserInfoSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    email = serializers.EmailField()
    name = serializers.CharField()
    user_type = serializers.IntegerField()
    permissions = PermissionSerializer(many=True)
