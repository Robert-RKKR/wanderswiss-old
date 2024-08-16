# Python - base import:
import uuid

# Django - user permission import:
from django.contrib.auth.models import PermissionsMixin

# Django - user models import:
from django.contrib.auth.models import AbstractBaseUser

# Django - translation model import:
from django.utils.translation import gettext_lazy as _

# Django - models import:
from django.db import models

# WanderSwiss - manager class import:
from management.managers.user_manager import UserModelManager

# WanderSwiss - choices import:
from wanderswiss.base.constants.user import UserRoleChoices

# WanderSwiss - base models import:
from wanderswiss.base.models.base_model import BaseModel


# User model class:
class UserModel(BaseModel, AbstractBaseUser, PermissionsMixin):

    class Meta:
        
        # Model name values:
        verbose_name = _('User')
        verbose_name_plural = _('Users')

        # Overwrite default permissions:
        default_permissions = ()
        permissions = (
            ('read_write', 'Read and write access.'),
            ('read_only', 'Read only access')
        )

    # Model objects manager:
    objects = UserModelManager()
    
    # Username main login attribute declaration:
    USERNAME_FIELD = 'username'

    # Primary Key value:
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    # Model data time information:
    created = models.DateTimeField(
        verbose_name=_('Created'),
        help_text=_('The date and time when the administrator account was '
                    'initially created.'),
        auto_now_add=True,
    )
    updated = models.DateTimeField(
        verbose_name=_('Updated'),
        help_text=_('The date and time when the administrator account was '
                    'last updated.'),
        auto_now=True,
    )

    # Base administrator values:
    is_root = models.BooleanField(
        verbose_name=_('Root'),
        help_text=_('Indicates if the account is a root account. Root accounts '
                    'have the highest level of access and cannot be deleted '
                    'or modified.'),
        default=False,
    )
    is_active = models.BooleanField(
        verbose_name=_('Active'),
        help_text=_('Indicates if the account is active. Inactive accounts '
                    'have limited functionality and cannot perform most '
                    'actions.'),
        default=True,
    )
    is_staff = models.BooleanField(
        verbose_name=_('Staff status'),
        help_text=_('Indicates if the user is part of the staff, which provides '
                    'access to the administrative interface.'),
        default=False,
    )

    # User role value:
    role = models.IntegerField(
        choices = UserRoleChoices.choices,
        verbose_name = _('Role'),
        help_text = _('User role.'),
        default=UserRoleChoices.USER
    )

    # Main administrator information:
    username = models.CharField(
        verbose_name=_('Username'),
        help_text=_('The unique name of the administrator used for login '
                    'and identification.'),
        max_length=128,
        unique=True,
    )
    name = models.CharField(
        verbose_name=_('First name'),
        help_text=_('User first name.'),
        max_length=128,
        unique=True,
    )
    surname = models.CharField(
        verbose_name=_('Surname'),
        help_text=_('User family name.'),
        max_length=128,
        unique=True,
    )
    email = models.EmailField(
        verbose_name=_('E-mail'),
        help_text=_('The unique email address of the administrator used for '
                    'communication and account recovery purposes.'),
        max_length=255,
        unique=True,
    )

    # Password information:
    password_to_change = models.BooleanField(
        verbose_name=_('Password change required'),
        help_text=_('Indicates if the user is required to change their '
                    'password upon next login.'),
        default=False,
    )

    def set_password(self, raw_password):
        """
        Set the password for the user. Also sets `password_to_change` to False.
        """

        self.password_to_change = False
        super().set_password(raw_password)
