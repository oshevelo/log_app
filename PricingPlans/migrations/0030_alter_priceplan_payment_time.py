# Generated by Django 3.2.7 on 2021-12-02 17:53

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('PricingPlans', '0029_alter_priceplan_payment_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='priceplan',
            name='payment_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 2, 17, 53, 4, 174597, tzinfo=utc), verbose_name='payment time'),
        ),
    ]
