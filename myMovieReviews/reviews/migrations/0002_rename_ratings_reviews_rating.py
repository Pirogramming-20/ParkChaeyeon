# Generated by Django 5.0.1 on 2024-01-12 09:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reviews',
            old_name='ratings',
            new_name='rating',
        ),
    ]
