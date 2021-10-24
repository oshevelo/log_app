from django.contrib.auth.models import User
from django.db import models


class Message(models.Model):
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


class GroupChats(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='group_chats')
    name = models.TextField('body', max_length=200)
    description = models.TextField('body', max_length=2000)
    image = models.ImageField(upload_to='images/group_avatar', default='images/group_avatar/default.png')

    class Meta:
        verbose_name = 'group_chats'
