from team.views import (AddTeamMembers, CustomCreateTeam, DeleteTeam, UpdateTeam, 
ViewTeamList)
from django.urls import path

urlpatterns = [
    path('create-team/',CustomCreateTeam.as_view(),name='create-team'),
    path('list-teams/',ViewTeamList.as_view(),name='list-teams'),
    path('add-members/<int:pk>/',AddTeamMembers.as_view(),name='add-members'),
    path('delete-team/<int:pk>/',DeleteTeam.as_view(), name='delete-team'),\
    path('update-team/<int:pk>',UpdateTeam.as_view(), name='update-team'),
]