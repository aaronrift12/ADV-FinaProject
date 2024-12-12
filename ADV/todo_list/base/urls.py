from django.urls import path
from rest_framework import routers
from .views import (
    TaskList, TaskDetail, TaskCreate, TaskUpdate, DeleteView,
    CustomLoginView, RegisterPage,
    TaskAPIView, TaskDetailAPIView
)
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'), 
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),
    path('', TaskList.as_view(), name='tasks'),  # Tasks list page
    path('task/<int:pk>/', TaskDetail.as_view(), name='task'), 
    path('task-create/', TaskCreate.as_view(), name='task-create'),
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name='task-update'), 
    path('task-delete/<int:pk>/', DeleteView.as_view(), name='task-delete'), 

    # API endpoints
    path('api/tasks/', TaskAPIView.as_view(), name='api-tasks'),
    path('api/tasks/<int:pk>/', TaskDetailAPIView.as_view(), name='api-task-detail'),
]
