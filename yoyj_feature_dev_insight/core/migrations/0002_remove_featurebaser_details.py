# Generated by Django 5.1.1 on 2024-10-15 00:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='featurebaser',
            name='details',
        ),
    ]