# Generated by Django 3.2.8 on 2021-10-15 12:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion

LANGUAGES  = [
    {
        'name': 'Bash',
        'lang_code': 'bash',
        'slug': 'bash',
        'mime': 'application/x-sh',
        'file_extension': '.sh',
    },
    {
        'name': 'C',
        'lang_code': 'c',
        'slug': 'c',
        'mime': 'text/x-chdr',
        'file_extension': '.c',
    },
    {
        'name': 'C#',
        'lang_code': 'c#',
        'slug': 'c-sharp',
        'mime': 'text/plain',
        'file_extension': '.aspx,',
    },
    {
        'name': 'C++',
        'lang_code': 'c++',
        'slug': 'cpp',
        'mime': 'text/x-c++hdr',
        'file_extension': '.cpp',
    },
    #...
]

def add_languages(apps, schema_editor):
    Language = apps.get_model('djangobin', 'language')

    for lang in LANGUAGES:
        l = Language.objects.get_or_create(
            name = lang['name'],
            lang_code = lang['lang_code'],
            slug = lang['slug'],
            mime = lang['mime'],
            file_extension = lang['file_extension'],
        )

    print(l)

def remove_languages(apps, schema_editor):
    Language = apps.get_model('djangobin', 'Language')

    for lang in LANGUAGES:
        l = Language.objects.get(
            lang_code=lang['lang_code'],
        )

        l.delete()


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('djangobin', '0009_alter_author_user'),
    ]

    operations = [
        migrations.RunPython(
            add_languages,
            remove_languages
        )
    ]
