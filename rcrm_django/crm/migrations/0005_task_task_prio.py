# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0004_auto_20160105_2217'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='task_prio',
            field=models.CharField(default='STD', max_length=3, verbose_name='Приоритет заявки'),
        ),
    ]
