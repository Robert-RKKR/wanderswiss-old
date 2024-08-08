# Django - translation model import:
from django.utils.translation import gettext_lazy as _

# Django - models import:
from django.db import models

# WanderSwiss - base model import:
from wanderswiss.base.models.identification_model import IdentificationBaseModel

# WanderSwiss - models import:
from knowledge_base.models.category_model import CategoryModel


class ArticleModel(IdentificationBaseModel):

    class Meta:
        
        # Model name values:
        verbose_name = _('Article')
        verbose_name_plural = _('Articles')

        # Default ordering:
        ordering = ['-timestamp']

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
    author = models.ForeignKey(
        User, 
        on_delete = models.SET_NULL, 
        null = True, 
        blank = True, 
        verbose_name = _('Author')
    )

    # Model based values:
    content = models.TextField(
        verbose_name = _('Content')
    )
    state = models.BooleanField(
        default = True, 
        verbose_name = _('Published')
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

    def __str__(self):
        return self.title
