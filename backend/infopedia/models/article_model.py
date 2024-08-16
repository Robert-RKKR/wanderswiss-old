# Django - translation model import:
from django.utils.translation import gettext_lazy as _

# Django - models import:
from django.db import models

# WanderSwiss - base model import:
from wanderswiss.base.models.identification_model import IdentificationBaseModel
from wanderswiss.base.models.status_model import StatusBasedModel

# WanderSwiss - choices import:
from wanderswiss.base.constants.article import StatusChoices
from wanderswiss.base.constants.language import LanguageChoices

# WanderSwiss - models import:
from infopedia.models.category_model import CategoryModel


# WanderSwiss dedicated model:
class ArticleModel(
    StatusBasedModel,
    IdentificationBaseModel):

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
    content = models.TextField(
        verbose_name = _('Content'),
        help_text = _('Xxx.'),
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
        # Check if description has been provided:
        if not self.description:
            # Create description based on content:
            self.description = self.content[:123]
