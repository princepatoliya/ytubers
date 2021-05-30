# Generated by Django 3.2 on 2021-05-23 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact_form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('user_name', models.CharField(max_length=255)),
                ('user_contactno', models.CharField(max_length=255)),
                ('user_emailid', models.CharField(max_length=255)),
                ('companyname', models.CharField(max_length=255)),
                ('subject', models.CharField(max_length=255)),
                ('message', models.CharField(max_length=255)),
            ],
        ),
    ]