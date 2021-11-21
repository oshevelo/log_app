from datetime import timezone
from django.contrib.auth.models import User
from django.db import models
import django.utils.timezone

class BasicPlan(models.Model):
    payment_time = models.DateTimeField('payment time', default=django.utils.timezone.now())
    payer = models.ForeignKey(User, on_delete=models.RESTRICT)
    plan_cost = models.DecimalField(max_digits=5, decimal_places=2, default=50)

class ProPlan(models.Model):
    payment_time = models.DateTimeField('payment time', default=django.utils.timezone.now())
    payer = models.ForeignKey(User, on_delete=models.RESTRICT)
    plan_cost = models.DecimalField(max_digits=5, decimal_places=2, default=75)

class VipPlan(models.Model):
    payment_time = models.DateTimeField('payment time', default=django.utils.timezone.now())
    plan_cost = models.DecimalField(max_digits=5, decimal_places=2, default=99)
    payer = models.ForeignKey(User, on_delete=models.RESTRICT)



