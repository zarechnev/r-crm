# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0006_auto_20160302_1126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='create_comment',
            field=models.CharField(verbose_name='Комментарий', max_length=200),
        ),
    ]
