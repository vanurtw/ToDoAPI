from django.urls import path, include
from . import views

urlpatterns = [
    path('task-all/', views.TaskListView.as_view()),
    path('task-update/<int:pk>/', views.TaskListView.as_view()),
    path('user-auth/', include('rest_framework.urls')),
    path('user-register/', views.UserRegister.as_view()),
    path('task-detail/<int:pk>/', views.TaskDetail.as_view()),
    path('user/login/', views.LoginViewAPI.as_view()),

]
