# Generated by Django 2.1.5 on 2019-01-23 21:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0003_squashed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='build',
            name='description',
        ),
        migrations.RemoveField(
            model_name='classification',
            name='description',
        ),
        migrations.RemoveField(
            model_name='classification',
            name='sortkey',
        ),
        migrations.RemoveField(
            model_name='priority',
            name='sortkey',
        ),
    ]