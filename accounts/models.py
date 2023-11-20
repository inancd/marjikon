from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


# Create your models here.

class CustomUserManager(BaseUserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Email adresi gereklidir')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser için is_staff=True olmalıdır.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser için is_superuser=True olmalıdır.')

        return self._create_user(email, password, **extra_fields)
    


class CustomUser(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    is_seller = models.BooleanField(default=False)

    object = CustomUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
    
    def get_full_name(self):
        return self.email
    
    def get_short_name(self):
        return self.email


class PersonalInfo(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(_('first name'), max_length=30)
    last_name = models.CharField(_('last name'), max_length=150)
    birth_date = models.DateField(_('birth date'), null=True, blank=True)
    phone_number = models.CharField(_('phone number'), max_length=15)
    GENDER_CHOICES = [
        ('M', _('Male')),
        ('F', _('Female')),
        ('O', _('Other')),
    ]
    gender = models.CharField(_('gender'), max_length=1, choices=GENDER_CHOICES)

    def __str__(self):
        if self.first_name == "" :
            return self.user.email
        else: 
            return f"{self.first_name} {self.last_name}"
