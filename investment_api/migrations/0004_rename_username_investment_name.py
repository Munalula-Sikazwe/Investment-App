# Generated by Django 3.2.4 on 2021-06-27 22:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('investment_api', '0003_auto_20210627_2251'),
    ]

    operations = [
        migrations.RenameField(
            model_name='investment',
            old_name='username',
            new_name='name',
        ),
    ]
