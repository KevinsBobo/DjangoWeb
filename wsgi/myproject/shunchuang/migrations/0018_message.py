# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shunchuang', '0017_auto_20160528_0509'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('eid', models.AutoField(serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=30)),
                ('massage', models.TextField()),
                ('username', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=10)),
                ('reply', models.TextField(blank=True)),
                ('replyname', models.CharField(max_length=20, blank=True)),
            ],
        ),
    ]
