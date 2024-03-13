from django.urls import path, include
from . import views

urlpatterns = [
    path('task-all/', views.TaskListView.as_view()),
    path('user-auth/', include('rest_framework.urls')),

]