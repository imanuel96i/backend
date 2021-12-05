from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone

#Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    username = None
    email = models.EmailField(
        unique=True,
        max_length=254,
    )
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    mobile = models.IntegerField()
    date_joined = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELD = []