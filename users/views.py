from django.http import request
from django.shortcuts import redirect, render
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, FormView, UpdateView
from django.contrib.auth import get_user, login
from users.models import NewUser
from users.forms import UserRegistrationForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

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

class RegisterLead(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = 'users/register_lead.html'
    model = NewUser
    fields = ['full_name','postal_code','description','is_lead']
    success_url = reverse_lazy('all-users')

    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_staff


class AllUsers(LoginRequiredMixin,ListView):
    model = NewUser
    context_object_name = 'current_users'

class AllLeads(LoginRequiredMixin, UserPassesTestMixin, ListView):
    template_name = 'users/newuser_list.html'
    context_object_name = 'current_users'
    queryset = NewUser.objects.filter(is_lead = True)

    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_staff


class DetailedUser(LoginRequiredMixin ,DetailView):
    model = NewUser
    context_object_name = 'current_users'
    template_name = 'users/user_details.html'

class DeleteUser(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = NewUser
    context_object_name = 'user'
    success_url = reverse_lazy('all-users')

    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_staff

class UpdateUser(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = NewUser
    context_object_name = 'user'
    template_name = 'users/user_form.html'
    fields = ['full_name','description','postal_code','email']
    success_url = reverse_lazy('all-users')

    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_staff

class EditUser(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = 'users/user_form.html'
    fields = ['full_name','description','postal_code','email']

    def get_success_url(self):
        return reverse_lazy('user-detail', kwargs={'pk':self.request.user.id})

    def get_object(self):
        return self.request.user

    def test_func(self):
        return self.request.user.is_authenticated 