from datetime import timezone
from django.contrib.auth.models import User
from django.db import models
import django.utils.timezone


class PricePlanTypes(models.Model):
    base = 9
    pro = 25
    vip = 49


class PricePlan(models.Model):

    plans = [
        (PricePlanTypes.base, 'Base Plan'),
        (PricePlanTypes.pro, 'Pro Plan'),
        (PricePlanTypes.vip, 'Vip Plan'),
    ]
    payment_time = models.DateTimeField('payment time', default=django.utils.timezone.now())
    payer = models.ForeignKey(User, on_delete=models.RESTRICT)
    plan_type = models.CharField(max_length=100, choices=plans)