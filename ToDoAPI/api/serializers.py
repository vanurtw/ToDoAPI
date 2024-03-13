from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    content = serializers.CharField()
    completed = serializers.BooleanField()
    data_create = serializers.DateTimeField()
    data_update = serializers.DateTimeField()
    user = serializers.CharField(source='author.username')
