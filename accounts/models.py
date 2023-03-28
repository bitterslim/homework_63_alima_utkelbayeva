from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.db.models import TextChoices


class GenderChoice(TextChoices):
    MALE = 'Male'
    FEMALE = 'Female'
    NONE = 'None'
class Account(AbstractUser):
    username = models.CharField(unique=True, verbose_name='Username', null=False, blank=False, max_length=100)
    email = models.EmailField(null=False,blank=False, verbose_name='Email',)
    avatar = models.ImageField(null=False, blank=False, upload_to='user_photo', verbose_name='Avatar')
    name = models.CharField(max_length=100, null=True, blank=True)
    info = models.TextField(verbose_name='User info', null=True,blank=True)
    phone = models.CharField(max_length=70, null=True, blank=True)
    subs = models.ManyToManyField(verbose_name='Subscriptions',  related_name='subscribers',  blank=True, to='accounts.Account', null = True )
    gender = models.CharField(verbose_name='Gender', max_length=30, choices=GenderChoice.choices, default=GenderChoice.NONE)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = [
        'email',
        'avatar',
    ]

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'