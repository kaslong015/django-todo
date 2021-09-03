from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Task
from django.urls import reverse_lazy
# Create your views here.


class TaskList (ListView):
    models = Task
    context_object_name = "tasks"

    # get query set to retrieve data
    def get_queryset(self):
        """Return all details in data base"""
        return Task.objects.all()


class TaskDetails (DetailView):
    model = Task
    context_object_name = "task"
    template_name = 'base/task.html'


class CreateTask (CreateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')


class UpdateTask (UpdateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')


class DeleteTask (DeleteView):
    model = Task
    context_object_name = 'tasks'
    success_url = reverse_lazy('tasks')
