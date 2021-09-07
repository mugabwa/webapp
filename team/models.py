from django.db import models
from django.utils import timezone

# Create your models here.
class Team(models.Model):
    team_name = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    start_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.team_name