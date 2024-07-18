# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2024-05-15 18:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0047_testattendance_mdlgrade'),
        ('training', '0012_auto_20240515_1424'),
    ]

    operations = [
        migrations.AddField(
            model_name='participant',
            name='city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='events.City'),
        ),
        migrations.AddField(
            model_name='participant',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='training.Company'),
        ),
    ]