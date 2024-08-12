# Django - translation model import:
from django.utils.translation import gettext_lazy as _

# Django - models import:
from django.db import models

# WanderSwiss - base model import:
from wanderswiss.base.models.identification_model import IdentificationBaseModel

# WanderSwiss - choices import:
from wanderswiss.base.constants.article import StatusChoices
from wanderswiss.base.constants.language import LanguageChoices

# WanderSwiss - models import:
from infopedia.models.category_model import CategoryModel


class ArticleModel(IdentificationBaseModel):

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
        null = True, 
        blank = True, 
        verbose_name = _('Category'),
        help_text = _('Xxx.'),
    )

    # Status related values:
    status = models.IntegerField(
        choices=StatusChoices.choices,
        verbose_name = _('Status'),
        help_text = _('Xxx.'),
        default=StatusChoices.DRAFT
    )
    published = models.DateTimeField(
        null = True, 
        blank = True, 
        verbose_name = _('Publish Down'),
        help_text = _('Xxx.'),
    )

    # Access related values:
    access = models.IntegerField(
        default = 1, 
        verbose_name = _('Access Level'),
        help_text = _('Xxx.'),
    )

    # Content related values:
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
        default=0,
        verbose_name = _('Counted visits'),
        help_text = _('Xxx.')
    )
