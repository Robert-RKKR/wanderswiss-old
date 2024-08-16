# Django - translation import:
from modeltranslation.translator import TranslationOptions
from modeltranslation.translator import translator

# WanderSwiss - model import:
from infopedia.models.choice_model import ChoiceModel


# Translation class:
class ChoiceTranslation(TranslationOptions):
    fields = ('name', 'content', 'description',)


# Register translation:
translator.register(ChoiceModel, ChoiceTranslation)
