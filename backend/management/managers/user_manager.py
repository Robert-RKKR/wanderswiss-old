# Django - user models import:
from django.contrib.auth.models import BaseUserManager

# WanderSwiss - choices import:
from wanderswiss.base.constants.user import UserRoleChoices


# User model manager class:
class UserModelManager(BaseUserManager):
    """ Manager for users. """

    # Django backward compatibility create user method:
    def create_user(self,username, email, password=None, **extra_fields):
        """Create, save and return a new user."""
        administrator = self.model(
            username=username, email=email, **extra_fields)
        administrator.set_password(password)
        administrator.save(using=self._db)
        return administrator
    
    # Django backward compatibility create super user method:
    def create_superuser(self, username, email, password):
        """Create and return a new superuser."""
        administrator = self.create_user(username, email, password)
        administrator.role = UserRoleChoices.ADMINISTRATOR
        administrator.is_staff = True
        administrator.is_superuser = True
        administrator.save(using=self._db)
        return administrator
    
    # WanderSwiss create user functions:
    def create_administrator(self, username, email, password):
        self.create_superuser(username, email, password)
    