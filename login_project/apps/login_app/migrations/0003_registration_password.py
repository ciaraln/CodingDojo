# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-23 03:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0002_auto_20180222_1651'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='password',
            field=models.CharField(default='default password', max_length=255),
            preserve_default=False,
        ),
    ]