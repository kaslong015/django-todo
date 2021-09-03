from django.urls import path
from . import views


urlpatterns = [
    path('', views.TaskList.as_view(), name="tasks"),
    path('task/<int:pk>/', views.TaskDetails.as_view(), name="task"),
    path('create-task/', views.CreateTask.as_view(), name="task-create"),
    path('update-task/<int:pk>/', views.UpdateTask.as_view(), name="update-task"),
    path('delete-task/<int:pk>/', views.DeleteTask.as_view(), name="delete-task"),
]
