# Generated by Django 3.2.3 on 2021-05-29 05:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('youtubers', '0004_youtuber_emailid'),
        ('hiretubers', '0004_alter_hiretuber_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hiretuber',
            name='user_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='youtubers.youtuber'),
        ),
    ]
