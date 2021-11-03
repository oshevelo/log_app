from django.contrib.auth.models import User
from django.db import models


class GroupChat(models.Model):
    name = models.TextField('name', max_length=200)
    description = models.TextField('description', max_length=2000)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_owner_chat', null=True, blank=True)
    participants = models.ManyToManyField(User, related_name='group_chat')
    image = models.ImageField(upload_to='images/group_avatar/%Y/%m/%d/', default='images/group_avatar/default.png',
                              blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Group chat'


class Message(models.Model):
    group_chat = models.ForeignKey('GroupChat', on_delete=models.CASCADE, verbose_name='Group Chat', db_index=True)
    sender = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='sender', related_name='from_user', db_index=True, null=True,
        blank=True
    )
    recipient = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='recipient', related_name='to_user', db_index=True, null=True,
        blank=True
    )
    timestamp = models.DateTimeField('timestamp', auto_now_add=True, editable=False)
    body = models.TextField('body', max_length=20000)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f'Message from {self.sender} to {self.recipient}'

    class Meta:
        verbose_name = 'message'
        verbose_name_plural = 'messages'
        ordering = ('-timestamp',)
