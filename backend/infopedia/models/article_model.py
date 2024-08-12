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
from management.models.user_model import UserModel


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
        verbose_name = _('Category')
    )

    # Model based values:
    content = models.TextField(
        verbose_name = _('Content')
    )
    published = models.DateTimeField(
        null = True, 
        blank = True, 
        verbose_name = _('Publish Down')
    )
    access = models.IntegerField(
        default = 1, 
        verbose_name = _('Access Level')
    )
    metadata = models.JSONField(
        default = dict, 
        blank = True, 
        verbose_name = _('Metadata')
    )

    status = models.IntegerField(
        choices=StatusChoices.choices,
        verbose_name = _('Xxx'),
        help_text = _('Xxx.'),
        default=StatusChoices.DRAFT
    )
    hits = models.IntegerField(
        default=0,
        verbose_name = _('Xxx'),
        help_text = _('Xxx.')
    )
    language = models.CharField(
        max_length=2,
        verbose_name = _('Xxx'),
        help_text = _('Xxx.'),
        choices=LanguageChoices,
        default=LanguageChoices.EN
    )
