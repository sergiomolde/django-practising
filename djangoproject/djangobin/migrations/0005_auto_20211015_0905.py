# Generated by Django 3.2.8 on 2021-10-15 07:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import djangobin.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('djangobin', '0004_auto_20211011_1443'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='active',
        ),
        migrations.RemoveField(
            model_name='author',
            name='created_on',
        ),
        migrations.RemoveField(
            model_name='author',
            name='email',
        ),
        migrations.RemoveField(
            model_name='author',
            name='last_logged_in',
        ),
        migrations.RemoveField(
            model_name='author',
            name='name',
        ),
        migrations.AddField(
            model_name='author',
            name='default_expiration',
            field=models.CharField(choices=[('never', 'Never'), ('1 week', '1 week'), ('1 month', '1 month'), ('6 month', '6 month'), ('1 year', ' 1 year')], default='never', max_length=10),
        ),
        migrations.AddField(
            model_name='author',
            name='default_exposure',
            field=models.CharField(choices=[('public', 'Public'), ('unlisted', 'Unlisted'), ('private', 'Private')], default='public', max_length=10),
        ),
        migrations.AddField(
            model_name='author',
            name='default_language',
            field=models.ForeignKey(default=djangobin.models.get_default_language, on_delete=django.db.models.deletion.CASCADE, to='djangobin.language'),
        ),
        migrations.AddField(
            model_name='author',
            name='private',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='author',
            name='user',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='profile', to='auth.user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='author',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]
