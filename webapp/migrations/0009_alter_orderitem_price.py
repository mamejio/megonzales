# Generated by Django 4.2.7 on 2024-01-22 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0008_remove_orderitem_order_orderitem_customername_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=20, null=True),
        ),
    ]
