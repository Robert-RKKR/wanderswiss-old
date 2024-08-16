# Django - translation import:
from modeltranslation.translator import TranslationOptions
from modeltranslation.translator import translator

# WanderSwiss - model import:
from infopedia.models.tag_model import TagModel


# Translation class:
class TagTranslation(TranslationOptions):
    fields = ('name', 'description',)


# Register translation:
translator.register(TagModel, TagTranslation)
