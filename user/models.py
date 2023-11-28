from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone
from rest_framework_simplejwt.tokens import OutstandingToken
from django.db.models.signals import pre_delete
from django.dispatch import receiver


class CustomUserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(username, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=150, unique=True, blank=False,null=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    last_logout = models.DateTimeField(blank=True, null=True) 

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'

# @receiver(pre_delete, sender=CustomUser)
# def user_pre_delete(sender, instance, **kwargs):
#     if instance.last_logout:
#         # Revoking all outstanding tokens for the user
#         tokens = OutstandingToken.objects.filter(user=instance)
#         for token in tokens:
#             token.blacklist()
#     def __str__(self):
#         return self.username
