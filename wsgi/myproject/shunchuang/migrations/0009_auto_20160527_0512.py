# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shunchuang', '0008_auto_20160526_0907'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='email_show',
            field=models.BooleanField(default=True),
        ),
    ]
