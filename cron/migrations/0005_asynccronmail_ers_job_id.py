# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-05-27 06:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cron', '0004_auto_20210514_1459'),
    ]

    operations = [
        migrations.AddField(
            model_name='asynccronmail',
            name='ers_job_id',
            field=models.TextField(null=True),
        ),
    ]