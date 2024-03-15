from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import TaskSerializer, UserSerializers
from rest_framework import mixins
from rest_framework import permissions
from rest_framework.authentication import SessionAuthentication
from .models import Task
from rest_framework.urls import urlpatterns


# Create your views here.


class CustomAuthSession(SessionAuthentication):
    def enforce_csrf(self, request):
        return None


class TaskListView(generics.GenericAPIView, mixins.CreateModelMixin, mixins.ListModelMixin):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, pk):
        # task = Task.objects.filter(id=pk)
        # task.update(**request.data)
        instance = Task.objects.get(id=pk)
        serializer = TaskSerializer(instance=instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(author=self.request.user)
        else:
            serializer.save()

    def filter_queryset(self, queryset):
        if self.request.user.is_authenticated:
            queryset = queryset.filter(author=self.request.user)
        else:
            queryset = []
        return queryset


class UserRegister(APIView):
    def post(self, request):
        serializer = UserSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
