from django.urls import path 
from . import views

urlpatterns = [
    # path('',Task.as_view(), name='task-list'),
    path('tasks/', views.TaskListCreateView.as_view(), name='task-list-create'),
    # path('tasks/title/<str:title>/', views.TaskListCreateView.as_view(), name='task-list'),
    


    path('tasks/title/<str:title>/', views.TaskDetailView.as_view(), name='task-detail'),
]
