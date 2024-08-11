# Django - admin import:
from django.contrib import admin

# WanderSwiss - base admin models import:
from wanderswiss.base.admins.based_admin import BaseAdmin

# Capybara - infopedia model import:
from infopedia.models.category_model import CategoryModel
from infopedia.models.article_model import ArticleModel


# All admin classes:
@admin.register(CategoryModel)
class CategoryAdmin(BaseAdmin):

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
class ArticleAdmin(BaseAdmin):

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
