# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0011_remove_subtask_parent'),
    ]

    operations = [
        migrations.AddField(
            model_name='subtask',
            name='parent',
            field=models.ForeignKey(to='crm.Task', verbose_name='Parent task', default=0, related_name='parent_task'),
            preserve_default=False,
        ),
    ]
