from rest_framework import serializers
from .models import UserType, User


class UserTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserType
        fields = ['url', 'type']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'user_type', 'email', 'name', 'birthday']
