# Generated by Django 3.2.9 on 2021-11-26 23:15

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('PricingPlans', '0023_auto_20211127_0111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='priceplan',
            name='payment_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 26, 23, 15, 22, 435467, tzinfo=utc), verbose_name='payment time'),
        ),
    ]
