import time
from django.db import models
import datetime
from django.utils import timezone
from django.contrib.auth.models import User



class pay_check(models.Model):
    receipt_id = models.IntegerField() #под ним я подразумиваю id услуги
    pay_time = models.DateTimeField('payment time', default= timezone.now())
    payer = models.ForeignKey(User, on_delete=models.CASCADE)
    sum = models.DecimalField(max_digits=5, decimal_places=2)
    email = models.EmailField(default=None)

    def was_published_recently(self):
        return self.pay_check >= timezone.now() - datetime.timedelta(days=1)

