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


class TaskListView(generics.GenericAPIView, mixins.ListModelMixin):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    authentication_classes = [CustomAuthSession]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return Response({'status': 'ok'})
