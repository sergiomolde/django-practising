# Generated by Django 3.2.8 on 2021-10-19 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangobin', '0006_auto_20211019_1619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='language',
            name='slug',
            field=models.SlugField(default='16346573215913024', max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='snippet',
            name='slug',
            field=models.SlugField(default=84014622),
        ),
        migrations.AlterField(
            model_name='tag',
            name='slug',
            field=models.SlugField(default='16346573215913024', max_length=200, unique=True),
        ),
    ]
