# Generated by Django 3.2.8 on 2021-10-19 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangobin', '0001_auto_20211019_1359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='slug',
            field=models.SlugField(max_length=200, unique=True),
        ),
    ]
