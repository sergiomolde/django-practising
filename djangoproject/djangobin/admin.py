from django.contrib import admin
from django.db.models import fields
from . import models
from reversion.admin import VersionAdmin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

# Register your models here.
class LanguageAdmin(VersionAdmin):
    list_display = ('name', 'lang_code', 'slug', 'mime', 'created_on')
    search_fields = ['name', 'mime']
    ordering = ['name']
    list_filter = ['created_on']
    date_hierarchy = 'created_on'

class SnippetAdmin(VersionAdmin):
    list_display = ('language', 'title', 'expiration', 'exposure', 'user')
    search_fields = ['title', 'user']
    ordering = ['-created_on']
    list_filter = ['created_on']
    date_hierarchy = 'created_on'
    filter_horizontal = ('tags',)
    fields = ('title', 'original_code', 'expiration', 'exposure', 'slug', 'hits', 'language', 'user', 'tags')

class TagAdmin(VersionAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name',)

class AuthorInline(admin.StackedInline):
    model = models.Author

class CustomUserAdmin(UserAdmin):
    inlines = (AuthorInline, )
    
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.register(models.Language, LanguageAdmin)
admin.site.register(models.Snippet, SnippetAdmin)
admin.site.register(models.Tag, TagAdmin)
