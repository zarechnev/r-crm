# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0010_auto_20160607_1141'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subtask',
            name='parent',
        ),
    ]
