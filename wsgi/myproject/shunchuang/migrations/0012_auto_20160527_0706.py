# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-27 07:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shunchuang', '0011_auto_20160527_0626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='username',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]