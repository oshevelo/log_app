# Generated by Django 3.2.9 on 2021-11-26 23:11

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('PricingPlans', '0022_auto_20211127_0109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='priceplan',
            name='payment_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 26, 23, 11, 36, 266090, tzinfo=utc), verbose_name='payment time'),
        ),
        migrations.AlterField(
            model_name='priceplan',
            name='plan_type',
            field=models.CharField(choices=[(9, 'Base Plan'), (25, 'Pro Plan'), (49, 'Vip Plan')], max_length=50),
        ),
    ]
