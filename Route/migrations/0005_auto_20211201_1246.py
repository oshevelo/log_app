# Generated by Django 3.2.7 on 2021-12-01 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Route', '0004_auto_20211130_0301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='route',
            name='end_point_lat',
            field=models.DecimalField(decimal_places=2, max_digits=14),
        ),
        migrations.AlterField(
            model_name='route',
            name='end_point_long',
            field=models.DecimalField(decimal_places=2, max_digits=14),
        ),
        migrations.AlterField(
            model_name='route',
            name='start_point_lat',
            field=models.DecimalField(decimal_places=2, max_digits=14),
        ),
        migrations.AlterField(
            model_name='route',
            name='start_point_long',
            field=models.DecimalField(decimal_places=2, max_digits=14),
        ),
    ]
