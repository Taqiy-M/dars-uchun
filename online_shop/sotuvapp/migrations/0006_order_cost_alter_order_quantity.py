# Generated by Django 4.1.1 on 2022-09-21 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sotuvapp', '0005_alter_cart_cost_alter_cart_order_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='cost',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='order',
            name='quantity',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
