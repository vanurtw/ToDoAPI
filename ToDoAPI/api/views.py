from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import TaskSerializer
from rest_framework import mixins
from rest_framework import permissions
from rest_framework.authentication import SessionAuthentication
from .models import Task


# Create your views here.


class CustomAuthSession(SessionAuthentication):
    def enforce_csrf(self, request):
        return None


class TaskListView(generics.GenericAPIView, mixins.CreateModelMixin):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        queryset = Task.objects.all()
        serializer = TaskSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        return self.create(request)

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(author=self.request.user)
        else:
            serializer.save()
