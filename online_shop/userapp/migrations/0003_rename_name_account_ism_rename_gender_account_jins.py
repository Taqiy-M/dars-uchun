# Generated by Django 4.1.1 on 2022-09-19 15:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0002_rename_jins_account_gender_rename_ism_account_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='name',
            new_name='ism',
        ),
        migrations.RenameField(
            model_name='account',
            old_name='gender',
            new_name='jins',
        ),
    ]
