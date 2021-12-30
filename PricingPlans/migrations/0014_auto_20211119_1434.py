# Generated by Django 3.2.7 on 2021-11-19 12:34

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('PricingPlans', '0013_auto_20211117_1938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicplan',
            name='payer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='basicplan',
            name='payment_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 19, 12, 34, 0, 264900, tzinfo=utc), verbose_name='payment time'),
        ),
        migrations.AlterField(
            model_name='proplan',
            name='payer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='proplan',
            name='payment_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 19, 12, 34, 0, 264900, tzinfo=utc), verbose_name='payment time'),
        ),
        migrations.AlterField(
            model_name='vipplan',
            name='payer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='vipplan',
            name='payment_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 19, 12, 34, 0, 264900, tzinfo=utc), verbose_name='payment time'),
        ),
    ]
