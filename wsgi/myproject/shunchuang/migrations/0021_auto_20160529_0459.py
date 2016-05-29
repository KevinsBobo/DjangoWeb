# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shunchuang', '0020_crowdfund_news'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='massage',
            new_name='message',
        ),
    ]
