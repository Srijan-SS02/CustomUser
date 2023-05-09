# class car(models.Model):
#     pass
#  ###to get all instance of car we use car.objects.all()

# class car(models.Model):
#     Cars=mdoels.Manger

# ###to get all instance of car now we need to write car.Cars.objects.all()

from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext as _

class CustomUserManager(BaseUserManager):
    
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError(_("User must have an email address"))
        email=self.normalize_email(email)     #normalize is to make case-Insensitive after @ in gmail
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        
        if extra_fields.get('is_staff') is not True:
            raise ValueError(_("Superuser must have its is_staff=True"))

        if extra_fields.get('is_active') is not True:
            raise ValueError(_("Superuser must have its is_active=True"))
        
        return self.create_user(email, password, **extra_fields)
    
        
        
        
        
        
        
        