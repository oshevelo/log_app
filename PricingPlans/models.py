from datetime import timezone
from django.contrib.auth.models import User
from django.db import models
import django.utils.timezone

class PricePlan(models.Model):

    plans = [
        ("BasePlan", 'Base Plan'),
        ("ProPlan", 'Pro Plan'),
        ("VipPlan", 'Vip Plan'),
    ]
    payment_time = models.DateTimeField('payment time', default=django.utils.timezone.now())
    payer = models.ForeignKey(User, on_delete=models.RESTRICT)
    plan_type = models.CharField(max_length=100, choices=plans)