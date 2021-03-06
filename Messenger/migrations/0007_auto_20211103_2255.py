# Generated by Django 3.2.7 on 2021-11-03 20:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Messenger', '0006_auto_20211031_1702'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='is_received',
        ),
        migrations.RemoveField(
            model_name='message',
            name='user',
        ),
        migrations.AddField(
            model_name='message',
            name='sender',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='from_user', to='auth.user', verbose_name='sender'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='groupchat',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_owner_chat', to=settings.AUTH_USER_MODEL),
        ),
    ]
