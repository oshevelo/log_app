# Generated by Django 3.2.7 on 2021-11-17 17:38

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('PaymentSystem', '0016_alter_paycheck_pay_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paycheck',
            name='pay_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 17, 17, 38, 49, 685079, tzinfo=utc), verbose_name='payment time'),
        ),
    ]
