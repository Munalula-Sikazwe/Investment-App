# Generated by Django 3.2.4 on 2021-06-27 23:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('investment_api', '0005_rename_name_investment_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='investment',
            old_name='investmentreturns',
            new_name='investmentReturns',
        ),
    ]