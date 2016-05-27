# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shunchuang', '0007_auto_20160522_0411'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='email_show',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='phone_show',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='sex',
            field=models.CharField(max_length=4, blank=True),
        ),
    ]
