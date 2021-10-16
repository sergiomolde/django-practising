# Generated by Django 3.2.8 on 2021-10-15 11:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('djangobin', '0006_remove_author_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='snippet',
            name='author',
        ),
        migrations.AddField(
            model_name='snippet',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
    ]
