# Django - admin import:
from django.contrib import admin

# WanderSwiss - base admin models import:
from wanderswiss.base.admins.based_admin import BaseTranslationAdmin

# WanderSwiss - infopedia model import:
from infopedia.models.category_model import CategoryModel
from infopedia.models.article_model import ArticleModel
from infopedia.models.choice_model import ChoiceModel
from infopedia.models.tag_model import TagModel

# WanderSwiss - translation import:
from infopedia.translation.category_translation import CategoryTranslation
from infopedia.translation.article_translation import ArticleTranslation
from infopedia.translation.choice_translation import ChoiceTranslation
from infopedia.translation.tag_translation import TagTranslation


# All admin classes:
@admin.register(CategoryModel)
class CategoryAdmin(BaseTranslationAdmin):

    list_display = (
        'name', 'is_active', 'created', 'updated',
    )
    list_display_links = (
        'name',
    )
    list_filter = (
        'is_active',
    )
    search_fields = (
        'name', 'description',
    )
    fieldsets = (
        ('Basic information', {
            'classes': ('wide', 'extrapretty',),
            'fields': ('is_active', 'created', 'updated', 'name', 'description',)
        }),
    )
    readonly_fields = (
        'created', 'updated',
    )
    empty_value_display = '--None--'


@admin.register(ArticleModel)
class ArticleAdmin(BaseTranslationAdmin):

    list_display = (
        'name', 'is_active', 'created', 'updated',
    )
    list_display_links = (
        'name',
    )
    list_filter = (
        'is_active',
    )
    search_fields = (
        'name', 'description',
    )
    fieldsets = (
        ('Base', {
            'classes': ('wide', 'extrapretty',),
            'fields': ('is_active', 'created', 'updated', 'name', 'description',
                        'category', 'status', 'published',)
        }),
        ('Access', {
            'classes': ('wide', 'extrapretty',),
            'fields': ('access',)
        }),
        ('Content', {
            'classes': ('wide', 'extrapretty',),
            'fields': ('content', 'metadata',)
        }),
        (' Statistic', {
            'classes': ('wide', 'extrapretty',),
            'fields': ('hits',)
        }),
    )
    readonly_fields = (
        'created', 'updated',
    )
    empty_value_display = '--None--'


@admin.register(ChoiceModel)
class ChoiceAdmin(BaseTranslationAdmin):

    list_display = (
        'name', 'is_active', 'created', 'updated',
    )
    list_display_links = (
        'name',
    )
    list_filter = (
        'is_active',
    )
    search_fields = (
        'name', 'description',
    )
    fieldsets = (
        ('Basic information', {
            'classes': ('wide', 'extrapretty',),
            'fields': ('is_active', 'created', 'updated', 'name', 'description',
                        'type',)
        }),
        ('Content', {
            'classes': ('wide', 'extrapretty',),
            'fields': ('content',)
        }),
        ('Localization', {
            'classes': ('wide', 'extrapretty',),
            'fields': ('latitude', 'longitude', 'range',)
        })
    )
    readonly_fields = (
        'created', 'updated',
    )
    empty_value_display = '--None--'


@admin.register(TagModel)
class TagAdmin(BaseTranslationAdmin):

    list_display = (
        'name', 'is_active', 'created', 'updated',
    )
    list_display_links = (
        'name',
    )
    list_filter = (
        'is_active',
    )
    search_fields = (
        'name', 'description',
    )
    fieldsets = (
        ('Basic information', {
            'classes': ('wide', 'extrapretty',),
            'fields': ('is_active', 'created', 'updated', 'name', 'description',)
        }),
    )
    readonly_fields = (
        'created', 'updated',
    )
    empty_value_display = '--None--'
