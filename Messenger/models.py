from django.contrib.auth.models import User
from django.db import models


class GroupChat(models.Model):
    name = models.TextField('name', max_length=200)
    description = models.TextField('description', max_length=2000, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_chats')
    participants = models.ManyToManyField(User)
    image = models.ImageField(upload_to='public/images/group_avatar/%Y/%m/%d/', default='images/group_avatar/default.png',
                              blank=True, null=True)

    class Meta:
        verbose_name = 'Group chat'


class Message(models.Model):
    group_chat = models.ForeignKey('GroupChat', on_delete=models.CASCADE, verbose_name='Group Chat', db_index=True)
    sender = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='sender', related_name='sent_messages',
                               db_index=True)
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='recipient',
                                  related_name='received_messages', db_index=True)
    timestamp = models.DateTimeField('timestamp', auto_now_add=True, editable=False)
    body = models.TextField('body', max_length=20000, blank=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f'Message from {self.sender} to {self.recipient}'

    class Meta:
        verbose_name = 'message'
        verbose_name_plural = 'messages'
        ordering = ('-timestamp',)
