# Generated by Django 3.2.8 on 2021-10-11 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangobin', '0002_auto_20211011_1241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='author',
            name='last_logged_in',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
