import datetime

from django.db import models
from django.utils import timezone


class Room(models.Model):
    room_text = models.CharField(max_length=12)
    pub_date = models.DateTimeField('date published')
    description = models.TextField(max_length=2000)

    def __str__(self):
        return self.room_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Message(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    message_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.message_text
