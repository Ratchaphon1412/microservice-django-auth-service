from typing import Any
import uuid
from django.db import models


from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import UserManager
from django.db import models

# Create your models here.




class UserProfilesManager(UserManager):
    def create_superuser(self, username, email, password=None, **extra_fields):
        if username is None:
            raise TypeError('Users should have a username')
        if email is None:
            raise TypeError('Users should have a email')
        
        user = self.model(username=username, email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.is_email_verified = False
        user.is_staff = True
        user.is_superuser = True
        user.save(self._db)
        return user
        
        
    def get_by_natural_key(self, username):
            return super().get_by_natural_key(username)
    
    

# Create your models here
class UserProfiles(AbstractBaseUser,PermissionsMixin):
    MALE = 'Male'
    FEMALE = 'Female'
    GENDER_IN_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=255)
    fullname = models.TextField( blank=True, null=True)
    email = models.EmailField(max_length=255, unique=True)
    profile = models.URLField(max_length=255, blank=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    gender = models.CharField(max_length=6, choices=GENDER_IN_CHOICES, null=True, blank=True)
    is_email_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    objects = UserProfilesManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
