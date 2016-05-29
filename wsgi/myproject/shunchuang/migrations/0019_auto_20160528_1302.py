# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shunchuang', '0018_message'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='eid',
            new_name='id',
        ),
    ]
