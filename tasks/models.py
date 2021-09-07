from django.db import models
from team.models import Team
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

# Create your models here.


class Task(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE,null=True,blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True,blank=True)
    start_date = models.DateTimeField()
    completion_date = models.DateTimeField()
    is_complete = models.BooleanField(default=False)

    def __str__(self):
        return self.title


    def clean(self):
        if self.start_date > self.completion_date:
            raise ValidationError(_('Start date %(val1)s cannot be surpass Completion date %(val2)s!'),
            params={'val1':self.start_date, 'val2':self.completion_date},
            )

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args,**kwargs)