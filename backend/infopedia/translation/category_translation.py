# Django - translation import:
from modeltranslation.translator import TranslationOptions
from modeltranslation.translator import translator

# WanderSwiss - model import:
from infopedia.models.category_model import CategoryModel


# Translation class:
class CategoryTranslation(TranslationOptions):
    fields = ('name', 'description',)


# Register translation:
translator.register(CategoryModel, CategoryTranslation)
