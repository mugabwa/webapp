from django.contrib.auth.views import LogoutView
from django.urls import path
from .views import AllLeads, AllUsers, CustomLoginView, DetailedUser, RegisterLead, RegisterUser

urlpatterns = [
    path('',AllUsers.as_view(), name='all-users'),
    path('user/<int:pk>', DetailedUser.as_view(), name='user-detail'),
    path('login',CustomLoginView.as_view(), name='login'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('logout',LogoutView.as_view(next_page='login'),name='logout'),
    path('register-lead/<int:pk>/',RegisterLead.as_view(),name='register-lead'),
    path('leads/',AllLeads.as_view(), name='leads'),
]