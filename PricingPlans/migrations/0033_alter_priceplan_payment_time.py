# Generated by Django 3.2.7 on 2021-12-02 21:43

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('PricingPlans', '0032_auto_20211202_2341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='priceplan',
            name='payment_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 2, 21, 43, 21, 326428, tzinfo=utc), verbose_name='payment time'),
        ),
    ]
