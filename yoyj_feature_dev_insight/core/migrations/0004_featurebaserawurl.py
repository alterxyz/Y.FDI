# Generated by Django 5.1.1 on 2024-10-17 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_featurebaser_last_sync_time_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeatureBaseRawUrl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.TextField()),
            ],
        ),
    ]
