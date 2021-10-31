from django.contrib.auth.models import User
from django.db import models


class GroupChat(models.Model):
    name = models.TextField('name', max_length=200)
    description = models.TextField('description', max_length=2000)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner_chat')
    participants = models.ManyToManyField(User, related_name='group_chat')
    image = models.ImageField(upload_to='images/group_avatar/%Y/%m/%d/', default='images/group_avatar/default.png')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super(GroupChat, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Group chat'


class Message(models.Model):
    group_chat = models.ForeignKey(GroupChat, on_delete=models.CASCADE, verbose_name='Group Chat', db_index=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='user', related_name='from_user', db_index=True
    )
    recipient = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='recipient', related_name='to_user', db_index=True
    )
    timestamp = models.DateTimeField('timestamp', auto_now_add=True, editable=False, db_index=True)
    body = models.TextField('body', max_length=20000)
    is_received = models.BooleanField(default=False)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f'Message from {self.user} to {self.recipient}'

    def save(self, *args, **kwargs):
        super(Message, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'message'
        verbose_name_plural = 'messages'
        ordering = ('-timestamp',)
