from rest_framework import serializers
from backend.models.user import User
from backend.models.coordinator import Coordinator


class CoordinatorSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Coordinator
        fields = ["id", "user", "created"]
