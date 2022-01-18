from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Notification(models.Model):
    EMAIL_NTF = "email"
    SMS_NTF = "sms"
    NTF_TYPE = [
        (EMAIL_NTF, 'Email'),
        (SMS_NTF, 'Sms'),
    ]
    ntf_type = models.CharField(
        choices=NTF_TYPE,
        default=EMAIL_NTF,
        max_length=50
    )
    subject = models.CharField(max_length=100)
    message = models.CharField(max_length=999)
    recipient = models.ForeignKey(User, related_name="ntf_to", on_delete=models.CASCADE, null=True)
    owner = models.ForeignKey(User, related_name="ntf_from", on_delete=models.CASCADE, null=True)
    date = models.DateTimeField(default=timezone.now)
