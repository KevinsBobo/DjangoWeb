# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shunchuang', '0019_auto_20160528_1302'),
    ]

    operations = [
        migrations.CreateModel(
            name='Crowdfund',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('url', models.CharField(max_length=60, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('url', models.CharField(max_length=60, blank=True)),
            ],
        ),
    ]
