# Generated by Django 3.1.7 on 2021-04-15 14:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kalendarzapp', '0002_auto_20210415_1412'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Meetings',
            new_name='Meeting',
        ),
    ]