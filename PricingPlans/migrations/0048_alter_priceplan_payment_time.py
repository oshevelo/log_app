# Generated by Django 3.2.7 on 2021-12-04 20:03

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('PricingPlans', '0047_alter_priceplan_payment_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='priceplan',
            name='payment_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 4, 20, 3, 3, 549954, tzinfo=utc), verbose_name='payment time'),
        ),
    ]
