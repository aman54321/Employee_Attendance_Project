from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager
# Create your models here.
class Employee(models.Model):
    emp_id = models.IntegerField()
    name = models.CharField(max_length=20)
    date = models.DateField()
    check_in = models.TimeField()
    check_out = models.TimeField()
    

    def __str__(self):
        return self.name
    
class Register(models.Model):
    e_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    username = models.CharField(max_length=20)
    designation = models.CharField(max_length=20)
    password1 = models.CharField(max_length=15)
    password2 = models.CharField(max_length=15)

    # class Meta:
    #     permissions = ('can_add_user','can add user')


    def __str__(self):
        return self.username
    
class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("email address"), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email






