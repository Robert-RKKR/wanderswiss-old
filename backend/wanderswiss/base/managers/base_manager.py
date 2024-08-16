# Django - model import:
from django.db.models import Manager

# Django - models import:
from django.db import models

# WanderSwiss - choices import:
from wanderswiss.base.constants.user import UserRoleChoices


# User query set:
class UserQuerySet(models.QuerySet):

    def for_user(self, user):
        if user.role == UserRoleChoices.ADMINISTRATOR:
            return self.all()
        elif user.role == UserRoleChoices.AUTHOR:
            return self.filter(created_by=user)
        elif user.role == UserRoleChoices.USER:
            # return self.filter(created_by=user, app='Hiking'
            return self.filter(created_by=user)
        return self.none()


# Base manager class:
class BaseManager(Manager):

    def get_queryset(self):
        return UserQuerySet(self.model, using=self._db)

    def for_user(self, user):
        return self.get_queryset().for_user(user)

