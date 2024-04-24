# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2022-07-05 09:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('creation', '0020_auto_20220328_1607'),
    ]

    operations = [
        migrations.AddField(
            model_name='fosscategory',
            name='csc_dca_programme',
            field=models.BooleanField(default=True, help_text='If unchecked, this foss will not be available for csc-dca programme'),
        ),
        migrations.AlterField(
            model_name='fosscategory',
            name='available_for_jio',
            field=models.BooleanField(default=True, help_text='If unchecked, this foss will not be available for jio, csc and spoken-tutorial.in'),
        ),
    ]