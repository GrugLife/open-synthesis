# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-24 20:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('openach', '0026_digeststatus_last_attempt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='digeststatus',
            name='last_attempt',
            field=models.DateTimeField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='digeststatus',
            name='last_success',
            field=models.DateTimeField(default=None, null=True),
        ),
    ]
