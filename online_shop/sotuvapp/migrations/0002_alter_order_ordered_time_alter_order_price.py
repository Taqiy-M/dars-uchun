# Generated by Django 4.1.1 on 2022-09-16 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sotuvapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='ordered_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='price',
            field=models.PositiveBigIntegerField(blank=True, null=True),
        ),
    ]
