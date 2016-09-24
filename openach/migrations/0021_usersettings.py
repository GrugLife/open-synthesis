# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-24 18:30
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import openach.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('openach', '0020_auto_20160923_0141'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('digest_frequency', models.PositiveSmallIntegerField(choices=[(openach.models.DigestFrequency(0), 'Never'), (openach.models.DigestFrequency(1), 'Daily'), (openach.models.DigestFrequency(2), 'Weekly')], default=openach.models.DigestFrequency(0), verbose_name='email digest frequency')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
