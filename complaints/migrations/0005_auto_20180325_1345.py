# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-25 13:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('complaints', '0004_auto_20180322_0617'),
    ]

    operations = [
        migrations.AddField(
            model_name='complaints',
            name='resolved',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='complaints',
            name='taken',
            field=models.BooleanField(default=False),
        ),
    ]