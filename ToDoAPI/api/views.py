from django.shortcuts import render, get_object_or_404
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
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)

    def filter_queryset(self, queryset):
        if self.request.user.is_authenticated:
            queryset = queryset.filter(author=self.request.user)
        return queryset

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class UserRegister(APIView):
    def post(self, request):
        serializer = UserSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class TaskDetail(generics.GenericAPIView):
    serializer_class = TaskSerializer
    def get(self, request, pk):
        try:
            task = Task.objects.get(pk=pk)
        except:
            return Response({'error':'no task'})
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    def put(self, request, pk):
        instance = get_object_or_404(Task, pk=pk)
        serializer = TaskSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk):
        try:
            instance = Task.objects.get(pk=pk)
        except:
            return Response({'error': 'no task'})
        instance.delete()
        return Response({'status': f'task {pk} delete'})
