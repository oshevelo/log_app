# Generated by Django 3.2.9 on 2021-11-26 20:24

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('PricingPlans', '0019_auto_20211126_2156'),
    ]

    operations = [
        migrations.CreateModel(
            name='PricePlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_time', models.DateTimeField(default=datetime.datetime(2021, 11, 26, 20, 24, 55, 118770, tzinfo=utc), verbose_name='payment time')),
                ('plan_type', models.CharField(choices=[(9, 'Base Plan'), (25, 'Pro Plan'), (49, 'Vip Plan')], default=None, max_length=3)),
                ('plan_cost', models.DecimalField(decimal_places=2, default=50, max_digits=5)),
                ('payer', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='proplan',
            name='payer',
        ),
        migrations.RemoveField(
            model_name='vipplan',
            name='payer',
        ),
        migrations.DeleteModel(
            name='BasicPlan',
        ),
        migrations.DeleteModel(
            name='ProPlan',
        ),
        migrations.DeleteModel(
            name='VipPlan',
        ),
    ]
