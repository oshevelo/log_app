# Generated by Django 3.2.7 on 2021-11-03 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Route', '0002_auto_20211103_2239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='route',
            name='date_time',
            field=models.DateTimeField(),
        ),
    ]
