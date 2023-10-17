from rest_framework import serializers
from backend.models.permission import Permission


class PermissionSerializer(serializers.ModelSerializer):
    resource = serializers.CharField(source='get_resource_display')
    can_write = serializers.BooleanField()
    can_read = serializers.BooleanField()

    class Meta:
        model = Permission
        fields = ["resource", "can_write", "can_read"]
