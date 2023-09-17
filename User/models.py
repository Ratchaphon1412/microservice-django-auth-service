import uuid
from django.db import models


from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import UserManager
from django.db import models

# Create your models here.




class UserProfilesManager(UserManager):
    pass
    # def get_by_natural_key(self, username):
    #         return super().get_by_natural_key(username)
    
    

# Create your models here
class UserProfiles(AbstractBaseUser):
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
    objects = UserProfilesManager()
    
    USERNAME_FIELD = 'email'
