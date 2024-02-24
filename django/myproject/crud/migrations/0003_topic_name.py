# Generated by Django 5.0.1 on 2024-02-17 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0002_topic_dt'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='name',
            field=models.CharField(default='名前', max_length=10, verbose_name='投稿者の名前'),
            preserve_default=False,
        ),
    ]