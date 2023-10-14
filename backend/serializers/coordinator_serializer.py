from rest_framework import serializers
from backend.models import User, Coordinator


class CoordinatorSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Coordinator
        fields = ["id", "user", "created"]
