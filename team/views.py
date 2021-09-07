from django.db import transaction
from django.views.generic.detail import DetailView
from users.models import NewUser
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from .models import Team
LIST_TEAM = 'team/list_team.html'

# Create your views here.
class CustomCreateTeam(LoginRequiredMixin, CreateView):
    template_name = 'team/create_team.html'
    model = Team
    fields = ['team_name','description']
    success_url = reverse_lazy('all-users')

class ViewTeamList(LoginRequiredMixin, ListView):
    template_name = LIST_TEAM
    model = Team
    context_object_name = 'teams'

class AddTeamMembers(LoginRequiredMixin,DetailView):
    template_name = 'team/add_members.html'
    model = Team
    context_object_name = 'team'
    def get_context_data(self, *args, **kwags):
        context = super(AddTeamMembers, self).get_context_data(*args, **kwags)
        context['members'] = NewUser.objects.all()
        return context
    def post(self, request, *args, **kwargs):
        for key, value in zip(request.POST.getlist('personid'),request.POST.getlist('teamid')):
            with transaction.atomic():
                to_update = NewUser.objects.filter(pk=key)
                if 'remove' in request.POST:
                    to_update.update(team=None)
                if 'add' in request.POST:
                    to_update.update(team=value)

        return super(AddTeamMembers, self).get(request,*args,**kwargs)


        

class DeleteTeam(LoginRequiredMixin,DeleteView):
    model = Team
    context_object_name = 'team'
    success_url = reverse_lazy(LIST_TEAM)

class UpdateTeam(LoginRequiredMixin,UpdateView):
    model = Team
    context_object_name = 'team'
    template_name = 'team/team_form.html'
    fields = ['team_name','description']
    success_url = reverse_lazy(LIST_TEAM)



