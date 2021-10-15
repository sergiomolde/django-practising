from django.contrib import admin
from . import models
from reversion.admin import VersionAdmin

# Register your models here.
@admin.register(models.Language)
class LanguageAdmin(VersionAdmin):
    list_display = ('name', 'lang_code', 'slug', 'mime', 'created_on')
    search_fields = ['name', 'mime']
    ordering = ['name']
    list_filter = ['created_on']
    date_hierarchy = 'created_on'

@admin.register(models.Snippet)
class SnippetAdmin(VersionAdmin):
    list_display = ('language', 'title', 'expiration', 'exposure', 'author')
    search_fields = ['title', 'author']
    ordering = ['-created_on']
    list_filter = ['created_on']
    date_hierarchy = 'created_on'
    filter_horizontal = ('tags',)

@admin.register(models.Tag)
class TagAdmin(VersionAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name',)

# @admin.register(models.Author)
# class AuthorAdmin(VersionAdmin):
#     list_display = ('name', 'email', 'active')
#     search_fields = ('name',)
#     list_filter = ['created_on']
#     date_hierarchy = 'created_on'
    