from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext as _
# Create your models here.

from .managers import CustomUserManager

class CustomUser(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    first_name=models.CharField(max_length=200,null=False,default="")
    last_name=models.CharField(max_length=200,null=False,default="")
    username=None
    
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS= []
    
    objects = CustomUserManager()
    
    def __str__(self):
        return self.first_name