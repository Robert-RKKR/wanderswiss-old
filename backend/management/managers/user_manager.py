# Django - user models import:
from django.contrib.auth.models import BaseUserManager


# User model manager class:
class UserModelManager(BaseUserManager):
    """ Manager for users. """

    def create_user(self, name, email, password=None, **extra_fields):
        """Create, save and return a new user."""
        administrator = self.model(name=name, email=email, **extra_fields)
        administrator.set_password(password)
        administrator.save(using=self._db)
        return administrator
    
    def create_superuser(self, name, email, password):
        """Create and return a new superuser."""
        administrator = self.create_user(name, email, password)
        administrator.is_staff = True
        administrator.is_superuser = True
        administrator.save(using=self._db)
        return administrator
    