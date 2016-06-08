# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0012_subtask_parent'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='is_subtask',
            field=models.BooleanField(default=False, verbose_name='Is SubTask'),
        ),
    ]
