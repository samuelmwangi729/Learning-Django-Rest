from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import UserManager
from Institutions.models import Institution
# Create your models here.
class CustomUserManager(UserManager):
    '''
    Define the methods that will lead to creation of the normal user and a super user
    '''
    #define how the users will be created here 
    def create_user(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(username, email, password, **extra_fields)
    #define the super user creation here 
    def create_superuser(self, username, email=None, password=None, **extra_fields):
        institution_name = "Utumishi Girls Academy"
        institution = Institution.objects.get(institution_name=institution_name)
        extra_fields.setdefault("institution",institution)
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(username, email, password, **extra_fields)

class User(AbstractUser):
    email = models.EmailField(unique=True,blank=False)
    institution = models.ForeignKey(Institution,on_delete=models.SET_NULL,related_name="users",blank=True,null=True)
    
    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name",'last_name','username']
