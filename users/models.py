from django.db import models
from team.models import Team
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# Create your models here.
class CustomAccountManager(BaseUserManager):
    def create_user(self, full_name,email, username, password, **others):
        email = self.normalize_email(email)
        if not username:
            raise ValueError('You must enter a valid username')
        user = self.model(full_name=full_name, email=email,username=username,
        password=password,**others)
        user.set_password(password)
        user.save()
        return user
    def create_lead(self, full_name, email, username, password, **others):
        others.setdefault('is_active',True)
        others.setdefault('is_lead',True)
        return self.create_user(full_name, email, username, password, **others)

    def create_superuser(self, full_name, email, username, password, **others):
        others.setdefault('is_staff', True)
        others.setdefault('is_superuser', True)
        others.setdefault('is_active',True)

        if others.get('is_staff') is not True:
            raise ValueError('Superuser must  be assigned be staff')

        if others.get('is_superuser') is not True:
            raise ValueError('Superuser must  be assigned be powerful')
        return self.create_user(full_name, email, username, password, **others)


class NewUser(AbstractBaseUser, PermissionsMixin):
    full_name = models.CharField(max_length=150)
    email = models.EmailField(blank=True)
    username = models.CharField(max_length=150,unique=True)
    password = models.CharField(max_length=250)
    postal_code = models.CharField(max_length=50, blank=True)
    description = models.TextField(blank=True)
    start_date = models.DateTimeField(default=timezone.now)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_lead = models.BooleanField(default=False)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, null=True,blank=True)

    objects = CustomAccountManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['full_name','email']

    def __str__(self):
        return self.username

