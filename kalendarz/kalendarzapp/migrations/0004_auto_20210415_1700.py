# Generated by Django 3.1.7 on 2021-04-15 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kalendarzapp', '0003_auto_20210415_1655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meeting',
            name='comment',
            field=models.TextField(blank=True, null=True),
        ),
    ]
