# Generated by Django 4.1.1 on 2022-09-16 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asosiy', '0005_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='rate',
            field=models.IntegerField(default=3),
        ),
        migrations.AlterField(
            model_name='comment',
            name='sana',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
