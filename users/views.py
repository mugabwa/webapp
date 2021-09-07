from django.shortcuts import redirect, render
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView, UpdateView
from django.contrib.auth import login
from users.models import NewUser
from users.forms import UserRegistrationForm
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class CustomLoginView(LoginView):
    template_name = "users/login.html"
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('all-users')

class RegisterUser(FormView):
    template_name = 'users/register_user.html'
    form_class = UserRegistrationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('all-users')

    # redirect user on registation to home page
    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterUser, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('all-users')
        return super(RegisterUser, self).get(*args, **kwargs)

class RegisterLead(LoginRequiredMixin,UpdateView):
    template_name = 'users/register_lead.html'
    model = NewUser
    fields = ['full_name','postal_code','description','is_lead']
    success_url = reverse_lazy('all-users')

class CreateTeam(LoginRequiredMixin, UpdateView):
    template_name = 'users/create_team.html'
    model = NewUser
    fields = ['full_name','']


class AllUsers(LoginRequiredMixin,ListView):
    model = NewUser
    context_object_name = 'current_users'

class AllLeads(LoginRequiredMixin, ListView):
    template_name = 'users/newuser_list.html'
    context_object_name = 'current_users'
    queryset = NewUser.objects.filter(is_lead = True)


class DetailedUser(LoginRequiredMixin ,DetailView):
    model = NewUser
    context_object_name = 'current_users'
    template_name = 'users/user_details.html'

