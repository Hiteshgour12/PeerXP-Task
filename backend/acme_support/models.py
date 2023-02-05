from django.db import models

from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.db import models
# from datetime import datetime
from rest_framework_simplejwt.tokens import RefreshToken
# from django_countries.fields import CountryField
# Create your models here.


 # custom user models
class UserManager(BaseUserManager):
    def create_user(self, email,password=None , password2=None):
        """
        Creates and saves a User with the given email,name,tc,and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        """
        Creates and saves a superuser with the given email, name,tc and password.
        """
        user = self.create_user(
            email,
            password=password,
            
        )
        user.is_admin = True
        user.is_active =True
        user.name = 'admin'
        user.role = 'admin'
        user.save(using=self._db)
        return user


class Deparments(models.Model):
    name = models.CharField(max_length=220, unique=True)
    description = models.CharField(max_length=220)
    created_by = models.CharField(max_length=220)
    created_at = models.DateTimeField(auto_now_add=True)
    last_update_at = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     return str(self.last_update_at),str(self.created_at)

# Custom User Manager
class User(AbstractBaseUser):
    DESIG = [
        ('admin', 'admin'),
        ('user', 'user'),
        ]
    
    email = models.EmailField(
        verbose_name='Email',
        max_length=255,
        unique=True,
    )
    name = models.CharField(max_length=20,blank=False,null=False)
    mobile_number = models.CharField(max_length=17,blank=False)
    department = models.ForeignKey(Deparments, on_delete=models.CASCADE,blank=True,null=True)
    created_by = models.CharField(max_length=220)
    created_at = models.DateTimeField(auto_now_add=True)
    role = models.CharField(choices=DESIG, max_length=200, default='user')
    is_active = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    last_update_at = models.DateTimeField(auto_now=True)


    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return{
            'refresh':str(refresh),
            'access':str(refresh.access_token)
        }

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return self.is_admin

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin



class Tickets(models.Model):
    subject = models.CharField(max_length=220, unique=True)
    body_description = models.CharField(max_length=220)
    priority = models.CharField(max_length=220)
    created_by = models.CharField(max_length=220)
    created_at = models.DateTimeField(auto_now_add=True)
    last_update_at = models.DateTimeField(auto_now=True)