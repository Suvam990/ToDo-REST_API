# Generated by Django 5.2 on 2025-05-07 11:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='claeated_at',
            new_name='created_at',
        ),
    ]
