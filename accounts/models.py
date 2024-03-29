from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.utils.crypto import get_random_string
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
    GENDER_CHOICES = [
        ('M', _('Male')),
        ('F', _('Female')),
        ('O', _('Other')),
    ]
    gender = models.CharField(_('gender'), max_length=1, choices=GENDER_CHOICES)

    def __str__(self):
        if self.first_name == "":
            return self.user.email
        else: 
            return f"{self.first_name} {self.last_name}"


class CustomAddress(models.Model):
    user = models.ForeignKey('CustomUser', on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, blank=True)
    first_name = models.CharField(_('first name'), max_length=30)
    last_name = models.CharField(_('last name'), max_length=150)
    phone_number = models.CharField(_('phone number'), max_length=11)
    city = models.CharField(_('city'), max_length=100)
    district = models.CharField(_('state'), max_length=200)
    neighborhood = models.CharField(_('neighborhood'), max_length=100)
    address = models.TextField()
    address_title = models.CharField(max_length=100)

    BILING_TYPE_CHOICES = (
        ('personal', 'Bireysel'),
        ('corporate', 'Kurumsal')
    )
    billing_type = models.CharField(_('biling type'), blank=True, choices=BILING_TYPE_CHOICES, max_length=100)
    tax_number = models.CharField(_('tax number'), max_length=20, blank=True)
    tax_office = models.CharField(_('tax office'), max_length=100, blank=True)
    company_name = models.CharField(_('company name'), max_length=100, blank=True)

    def __str__(self):
        return f"{self.address_title} - {self.user.email}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.address_title)
        original_slug = self.slug
        counter = 1
        while CustomAddress.objects.filter(slug=self.slug).exclude(id=self.id).exists():
            self.slug = f'{original_slug}-{counter}'
            counter += 1
        super().save(*args, **kwargs)