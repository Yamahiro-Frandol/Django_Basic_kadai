# Generated by Django 5.0.1 on 2024-02-17 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0003_topic_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='file',
            field=models.FileField(default='test.png', upload_to='crud/topic/file/', verbose_name='ファイル'),
            preserve_default=False,
        ),
    ]
