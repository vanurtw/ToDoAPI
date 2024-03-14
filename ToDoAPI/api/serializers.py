from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    content = serializers.CharField()
    completed = serializers.BooleanField(read_only=True)
    data_create = serializers.DateTimeField(read_only=True)
    data_update = serializers.DateTimeField(read_only=True)
    user = serializers.CharField(source='author.username', read_only=True)

    def create(self, validated_data):
        return Task.objects.create(**validated_data)
