# Generated by Django 3.1.7 on 2021-04-15 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Meetings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.IntegerField(null=True)),
                ('month', models.IntegerField(null=True)),
                ('year', models.IntegerField(null=True)),
                ('user', models.CharField(max_length=50, null=True)),
                ('hour_start', models.IntegerField(null=True)),
                ('hour_stop', models.IntegerField(null=True)),
                ('minute_start', models.IntegerField(null=True)),
                ('minute_stop', models.IntegerField(null=True)),
                ('comment', models.TextField(null=True)),
            ],
        ),
    ]