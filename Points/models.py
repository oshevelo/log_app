from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(User, max_length=50, null=True, blank=True)
    first_name = models.CharField(User, max_length=100, null=True, blank=True)
    last_name = models.CharField(User, max_length=50, null=True, blank=True)
    email = models.EmailField(User, max_length=100, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()