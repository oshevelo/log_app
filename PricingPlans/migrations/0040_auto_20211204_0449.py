# Generated by Django 3.2.7 on 2021-12-04 02:49

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('PricingPlans', '0039_auto_20211204_0447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='priceplan',
            name='payer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='priceplan',
            name='payment_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 4, 2, 49, 33, 563943, tzinfo=utc), verbose_name='payment time'),
        ),
    ]
