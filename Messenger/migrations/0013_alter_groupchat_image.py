# Generated by Django 3.2.7 on 2021-12-04 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Messenger', '0012_auto_20211121_1708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groupchat',
            name='image',
            field=models.ImageField(blank=True, default='images/group_avatar/default.png', null=True, upload_to='public/images/group_avatar/%Y/%m/%d/'),
        ),
    ]
