from tasks.views import CreateTask, DeleteTask, ListTasks, SelectTeam, UpdateTask
from django.urls import path

urlpatterns = [
    path('task-list/',ListTasks.as_view(),name='task-list'),
    path('task-create/',CreateTask.as_view(),name='task-create'),
    path('task-delete/<int:pk>/',DeleteTask.as_view(),name='task-delete'),
    path('task-update/<int:pk>/',UpdateTask.as_view(),name='task-update'),
    path('task-assign/<int:pk>/',SelectTeam.as_view(),name='task-assign'), 
]