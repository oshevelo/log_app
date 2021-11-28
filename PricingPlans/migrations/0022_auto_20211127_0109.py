# Generated by Django 3.2.9 on 2021-11-26 23:09

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('PricingPlans', '0021_auto_20211127_0105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='priceplan',
            name='payment_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 26, 23, 9, 22, 8867, tzinfo=utc), verbose_name='payment time'),
        ),
        migrations.AlterField(
            model_name='priceplan',
            name='plan_type',
            field=models.CharField(choices=[(9, 'Base Plan - 9$'), (25, 'Pro Plan - 25$'), (49, 'Vip Plan - 49$')], default=None, max_length=3),
        ),
    ]
