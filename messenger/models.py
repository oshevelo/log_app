from django.contrib.auth.models import User
from django.db import models


class MessageModel(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='user', related_name='from_user', db_index=True
    )
    recipient = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='recipient', related_name='to_user', db_index=True
    )
    timestamp = models.DateTimeField('timestamp', auto_now_add=True, editable=False, db_index=True)
    body = models.TextField('body', max_length=20000)

    def __str__(self):
        return str(self.id)

    def save(self, *args, **kwargs):
        self.body = self.body.strip()
        super(MessageModel, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'message'
        verbose_name_plural = 'messages'
        ordering = ('-timestamp',)
