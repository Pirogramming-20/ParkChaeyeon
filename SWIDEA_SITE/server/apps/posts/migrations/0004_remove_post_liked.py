# Generated by Django 5.0.1 on 2024-01-17 10:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_post_liked'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='liked',
        ),
    ]
