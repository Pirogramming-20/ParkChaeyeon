# Generated by Django 5.0.1 on 2024-01-17 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='region',
        ),
        migrations.AddField(
            model_name='post',
            name='interest',
            field=models.IntegerField(default=0, verbose_name='관심도'),
        ),
    ]
