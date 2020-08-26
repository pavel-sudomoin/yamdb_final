from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.db import models


USERS_ROLES = (
    ('user', 'Simple user'),
    ('moderator', 'Website moderator'),
    ('admin', 'Administrator'),
)


class User(AbstractUser):
    """
    Custom User model with extra fields
    """

    email = models.EmailField(_('email address'), unique=True)
    bio = models.TextField(null=True, blank=True)
    role = models.CharField(max_length=10, choices=USERS_ROLES, default='user')
    confirmation_code = models.CharField(max_length=20, null=True, blank=True)

    @property
    def is_moderator(self):
        return self.role == 'moderator'

    @property
    def is_admin(self):
        return self.role == 'admin' or self.is_superuser

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ('email',)
