from django.db import transaction
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from .models import Task
from team.models import Team

# Create your views here.
class CreateTask(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['title','description','start_date','completion_date']
    success_url = reverse_lazy('task-list')

class ListTasks(LoginRequiredMixin,ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'tasks/task_list.html'

class DeleteTask(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('task-list')
    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_staff

class UpdateTask(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Task
    context_object_name = 'task'
    template_name = 'tasks/task_form.html'
    fields = ['description','start_date','completion_date','is_complete']
    success_url = reverse_lazy('task-list')

    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_staff


    
class SelectTeam(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Task
    template_name = 'tasks/task_assign.html'
    context_object_name = 'task'
    
    def get_success_url(self):
        return reverse_lazy('task-assign', kwargs={'pk':self.object.pk})
    
    def get_context_data(self, *args, **kwargs):
        context = super(SelectTeam, self).get_context_data(*args,**kwargs)
        context['teams'] = Team.objects.all()
        return context

    def post(self, request, *args, **kwargs):
        for key, value in zip(request.POST.getlist('taskid'),request.POST.getlist('teamid')):
            with transaction.atomic():
                to_update = Task.objects.filter(pk=key)
                if 'remove' in request.POST:
                    to_update.update(team=None)
                if 'add' in request.POST:
                    to_update.update(team=value)
        return super(SelectTeam, self).get(request, *args, **kwargs)

    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_staff
    
