# Generated by Django 3.2 on 2021-05-23 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtubers', '0003_auto_20210303_1913'),
    ]

    operations = [
        migrations.AddField(
            model_name='youtuber',
            name='emailid',
            field=models.CharField(default='', max_length=255),
        ),
    ]
