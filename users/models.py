from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.db import models


class UsersRoles(models.TextChoices):
    """
    User enum. Used as separate class, `cause it used in fixtures factories
    """

    USER = 'user', _('Simple user')
    MODERATOR = 'moderator', _('Website moderator')
    ADMIN = 'admin', _('Administrator')


class User(AbstractUser):
    """
    Custom User model with extra fields
    """

    email = models.EmailField(_('email address'), unique=True)
    bio = models.TextField(null=True, blank=True)
    role = models.CharField(
        max_length=100, choices=UsersRoles.choices, default=UsersRoles.USER
    )
    confirmation_code = models.CharField(max_length=50, null=True, blank=True)

    @property
    def is_moderator(self):
        return self.role == 'moderator'

    @property
    def is_admin(self):
        return self.role == 'admin' or self.is_superuser

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ('email',)
