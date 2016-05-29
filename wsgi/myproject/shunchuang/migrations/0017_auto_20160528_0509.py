# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shunchuang', '0016_auto_20160527_1431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='person_photo',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='select',
            field=models.CharField(max_length=6, choices=[('\u521b\u4e1a', '\u521b\u4e1a'), ('\u7ec4\u961f', '\u7ec4\u961f')]),
        ),
    ]
