from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import (
    BaseUserManager, AbstractUser
)


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where username is the unique identifiers
    """
    def create_user(self, username, password, **extra_fields):
        """
        Create and save a User with the given username and password.
        """
        if not username:
            raise ValueError(_('The username must be set.'))

        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, password, **extra_fields):
        """
        Create and save a SuperUser with the given username and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(username, password, **extra_fields)


class CustomUser(AbstractUser):
    # Removing some fields
    email = None
    first_name = None
    last_name = None

    # and adding new fields
    username = models.CharField(_('Username'), max_length=100, unique=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
    ordering = ['username']

    objects = CustomUserManager()

    def __str__(self):
        return self.username
