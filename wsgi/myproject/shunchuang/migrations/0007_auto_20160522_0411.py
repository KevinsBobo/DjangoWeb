# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shunchuang', '0006_auto_20160521_1342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='select',
            field=models.IntegerField(),
        ),
    ]
