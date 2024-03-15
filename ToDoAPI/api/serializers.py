from rest_framework import serializers
from .models import Task
from django.contrib.auth.models import User


class TaskSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255, read_only=True)
    content = serializers.CharField(read_only=True)
    completed = serializers.BooleanField(default=False)
    data_create = serializers.DateTimeField(read_only=True)
    data_update = serializers.DateTimeField(read_only=True)
    user = serializers.CharField(source='author.username', read_only=True)

    def create(self, validated_data):
        return Task.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.__dict__.update(**validated_data)
        instance.save()
        return instance


class UserSerializers(serializers.Serializer):
    username = serializers.CharField(max_length=200)
    email = serializers.EmailField(read_only=True)
    password = serializers.CharField(max_length=255)

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data.get('password'))
        user.save()
        return user
