# Django - translation model import:
from django.utils.translation import gettext_lazy as _

# Django - models import:
from django.db import models

# WanderSwiss - base model import:
from wanderswiss.base.models.identification_model import IdentificationBaseModel
from wanderswiss.base.models.language_model import LanguageBaseModel
from wanderswiss.base.models.status_model import StatusBasedModel

# WanderSwiss - choices import:
from wanderswiss.base.constants.article import StatusChoices
from wanderswiss.base.constants.language import LanguageChoices

# WanderSwiss - models import:
from infopedia.models.category_model import CategoryModel


# WanderSwiss dedicated model:
class ArticleModel(
    StatusBasedModel,
    IdentificationBaseModel,
    LanguageBaseModel):

    class Meta:
        
        # Model name values:
        verbose_name = _('Article')
        verbose_name_plural = _('Articles')

        # Default ordering:
        ordering = ['-created']

        # Overwrite default permissions:
        default_permissions = ()
        permissions = (
            ('read_write', 'Read and write access.'),
            ('read_only', 'Read only access')
        )

    
    # Relation with other models:
    category = models.ForeignKey(
        CategoryModel,
        on_delete = models.SET_NULL,
        verbose_name = _('Category'),
        help_text = _('Xxx.'),
        null = True,
        blank = True,
    )

    # Status related values:
    status = models.IntegerField(
        choices=StatusChoices.choices,
        verbose_name = _('Status'),
        help_text = _('Xxx.'),
        default=StatusChoices.DRAFT
    )
    published = models.DateTimeField(
        verbose_name = _('Publish Down'),
        help_text = _('Xxx.'),
        null = True,
        blank = True,
    )

    # Access related values:
    access = models.IntegerField(
        verbose_name = _('Access Level'),
        help_text = _('Xxx.'),
        default = 1,
    )

    # Content related values:
    introtext = models.TextField(
        verbose_name = _('Intro'),
        help_text = _('Xxx.'),
        null = True,
        blank = True,
    )
    content = models.TextField(
        verbose_name = _('Content'),
        help_text = _('Xxx.'),
    )
    language = models.CharField(
        max_length=2,
        verbose_name = _('Language'),
        help_text = _('Xxx.'),
        choices=LanguageChoices,
        default=LanguageChoices.EN
    )
    metadata = models.JSONField(
        default = dict, 
        blank = True, 
        verbose_name = _('Metadata'),
        help_text = _('Xxx.'),
    )

    # Statistic related values:
    hits = models.IntegerField(
        verbose_name = _('Counted visits'),
        help_text = _('Xxx.'),
        default=0,
    )

    def dedicated_operation(self):
        # Call the original dedicated_operation method:
        super().dedicated_operation()
        # Create introtext if not define:
        self.collect_introtext()

    def collect_introtext(self):
        # Check if introtext has been provided:
        print(f'self.introtext: {self.introtext}')
        if not self.introtext:
            # Create introtext based on content:
            self.introtext = self.content[:123]
