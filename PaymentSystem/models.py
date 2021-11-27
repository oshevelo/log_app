import time
from django.contrib.auth.models import User
from django.db import models
import datetime

from django.shortcuts import render
from django.utils import timezone




class PayCheck(models.Model):
    receipt_id = models.IntegerField() #под ним я подразумиваю id услуги
    pay_time = models.DateTimeField('payment time', default=timezone.now)
    payer = models.ForeignKey(User, on_delete=models.RESTRICT)
    sum = models.DecimalField(max_digits=5, decimal_places=2)
    email = models.EmailField(default=None)

    def was_published_recently(self):
        return self.PayCheck >= timezone.now() - datetime.timedelta(days=1)


def paytest(request):
    return render(request, "paymants/index.html")