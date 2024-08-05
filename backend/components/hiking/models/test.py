from django.db import models
from django.utils.translation import gettext_lazy as _

class CantonChoices(models.IntegerChoices):
    CANTON_1 = 1, _('Canton 1')
    CANTON_2 = 2, _('Canton 2')
    # Add other cantons as needed

class RoadTypeChoices(models.IntegerChoices):
    ROAD_TYPE_1 = 1, _('Road Type 1')
    ROAD_TYPE_2 = 2, _('Road Type 2')
    # Add other road types as needed

class CardModel(models.Model):
    name = models.CharField(
        max_length=255, 
        verbose_name=_('Name'), 
        help_text=_('Name of the card.')
    )
    description = models.TextField(
        verbose_name=_('Description'), 
        help_text=_('Description of the card.')
    )

    def __str__(self):
        return self.name


    def __str__(self):
        return self.name

class TrialModel(models.Model):
    id = models.CharField(
        primary_key=True, 
        max_length=255, 
        verbose_name=_('ID'), 
        help_text=_('Unique identifier for the trial.')
    )
    created = models.DateField(
        auto_now_add=True, 
        verbose_name=_('Created Date'), 
        help_text=_('Date when the trial was created.')
    )
    updated = models.DateField(
        auto_now=True, 
        verbose_name=_('Updated Date'), 
        help_text=_('Date when the trial was last updated.')
    )
    name = models.CharField(
        max_length=255, 
        verbose_name=_('Name'), 
        help_text=_('Name of the trial.')
    )
    slug = models.SlugField(
        unique=True, 
        verbose_name=_('Slug'), 
        help_text=_('Slug for the trial.')
    )
    description = models.TextField(
        verbose_name=_('Description'), 
        help_text=_('Description of the trial.')
    )
    routes = models.ManyToManyField(
        RouteModel, 
        through='TrialRouteModel', 
        verbose_name=_('Routes'), 
        help_text=_('Routes that are part of the trial.')
    )

    def __str__(self):
        return self.name

class TrialRouteModel(models.Model):
    trial = models.ForeignKey(
        TrialModel, 
        on_delete=models.CASCADE, 
        verbose_name=_('Trial'), 
        help_text=_('Trial that includes this route.')
    )
    route = models.ForeignKey(
        RouteModel, 
        on_delete=models.CASCADE, 
        verbose_name=_('Route'), 
        help_text=_('Route included in the trial.')
    )

    def __str__(self):
        return f"{self.trial.name} includes {self.route.name}"

class MultidayTrialModel(models.Model):
    id = models.CharField(
        primary_key=True, 
        max_length=255, 
        verbose_name=_('ID'), 
        help_text=_('Unique identifier for the multiday trial.')
    )
    created = models.DateField(
        auto_now_add=True, 
        verbose_name=_('Created Date'), 
        help_text=_('Date when the multiday trial was created.')
    )
    updated = models.DateField(
        auto_now=True, 
        verbose_name=_('Updated Date'), 
        help_text=_('Date when the multiday trial was last updated.')
    )
    name = models.CharField(
        max_length=255, 
        verbose_name=_('Name'), 
        help_text=_('Name of the multiday trial.')
    )
    slug = models.SlugField(
        unique=True, 
        verbose_name=_('Slug'), 
        help_text=_('Slug for the multiday trial.')
    )
    description = models.TextField(
        verbose_name=_('Description'), 
        help_text=_('Description of the multiday trial.')
    )
    trials = models.ManyToManyField(
        TrialModel, 
        through='MultidayTrialTrialModel', 
        verbose_name=_('Trials'), 
        help_text=_('Trials that are part of the multiday trial.')
    )
    days = models.IntegerField(
        verbose_name=_('Days'), 
        help_text=_('Number of days for the multiday trial.')
    )

    def __str__(self):
        return self.name

class MultidayTrialTrialModel(models.Model):
    trial = models.ForeignKey(
        TrialModel, 
        on_delete=models.CASCADE, 
        verbose_name=_('Trial'), 
        help_text=_('Trial included in the multiday trial.')
    )
    multiday_trial = models.ForeignKey(
        MultidayTrialModel, 
        on_delete=models.CASCADE, 
        verbose_name=_('Multiday Trial'), 
        help_text=_('Multiday trial that includes this trial.')
    )
    order = models.IntegerField(
        verbose_name=_('Order'), 
        help_text=_('Order of the trial within the multiday trial.')
    )

    def __str__(self):
        return f"{self.multiday_trial.name} includes {self.trial.name} in order {self.order}"

class UserModel(models.Model):
    username = models.CharField(
        max_length=255, 
        verbose_name=_('Username'), 
        help_text=_('Username of the user.')
    )
    email = models.EmailField(
        verbose_name=_('Email'), 
        help_text=_('Email address of the user.')
    )

    def __str__(self):
        return self.username

class UserRouteModel(models.Model):
    user = models.ForeignKey(
        UserModel, 
        on_delete=models.CASCADE, 
        verbose_name=_('User'), 
        help_text=_('User who accomplished the route.')
    )
    route = models.ForeignKey(
        RouteModel, 
        on_delete=models.CASCADE, 
        verbose_name=_('Route'), 
        help_text=_('Route that was accomplished.')
    )
    date_accomplished = models.DateField(
        verbose_name=_('Date Accomplished'), 
        help_text=_('Date when the route was accomplished.')
    )
    distance_covered_km = models.FloatField(
        verbose_name=_('Distance Covered (km)'), 
        help_text=_('Distance covered by the user in kilometers.')
    )
    additional_info = models.TextField(
        blank=True, 
        null=True, 
        verbose_name=_('Additional Information'), 
        help_text=_('Any additional information about the accomplishment.')
    )

    def __str__(self):
        return f"{self.user.username} accomplished {self
