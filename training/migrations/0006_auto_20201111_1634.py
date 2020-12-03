# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-11-11 11:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0005_auto_20200817_1240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainingevents',
            name='event_type',
            field=models.CharField(choices=[('', '-----'), ('FDP', 'Paid FDP'), ('Workshop', 'Blended Mode Workshop'), ('sdp', 'Student Training Programme'), ('TPDP', 'Teachers Professional Development Program'), ('SSDP', 'School Students  Development Program')], max_length=50),
        ),
    ]