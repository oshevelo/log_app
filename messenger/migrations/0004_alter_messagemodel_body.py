# Generated by Django 3.2.7 on 2021-10-09 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messenger', '0003_alter_messagemodel_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messagemodel',
            name='body',
            field=models.TextField(max_length=20000, verbose_name='body'),
        ),
    ]
