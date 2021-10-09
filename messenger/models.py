from django.contrib.auth.models import User
from django.db.models import Model, TextField, DateTimeField, ForeignKey, CASCADE


class MessageModel(Model):
    user = ForeignKey(User, on_delete=CASCADE, verbose_name='user', related_name='from_user', db_index=True)
    recipient = ForeignKey(User, on_delete=CASCADE, verbose_name='recipient', related_name='to_user', db_index=True)
    timestamp = DateTimeField('timestamp', auto_now_add=True, editable=False, db_index=True)
    body = TextField('body', max_length=20000)

    def __str__(self):
        return str(self.id)

    def characters(self):
        # Toy function to count body characters.
        # :return: body's char number
        return len(self.body)

    def save(self, *args, **kwargs):
        self.body = self.body.strip()  # Trimming whitespaces from the body
        super(MessageModel, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'message'
        verbose_name_plural = 'messages'
        ordering = ('-timestamp',)
