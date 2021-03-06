# Generated by Django 3.2.7 on 2021-11-16 21:01

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('PricingPlans', '0004_auto_20211113_2249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicplan',
            name='payment_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 16, 21, 1, 16, 713805, tzinfo=utc), verbose_name='payment time'),
        ),
        migrations.AlterField(
            model_name='proplan',
            name='payment_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 16, 21, 1, 16, 714803, tzinfo=utc), verbose_name='payment time'),
        ),
        migrations.AlterField(
            model_name='vipplan',
            name='payment_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 16, 21, 1, 16, 714803, tzinfo=utc), verbose_name='payment time'),
        ),
    ]
