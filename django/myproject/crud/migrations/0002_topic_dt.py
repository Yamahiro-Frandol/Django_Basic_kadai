# Generated by Django 5.0.1 on 2024-02-09 12:47

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='dt',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='投稿日時'),
        ),
    ]
