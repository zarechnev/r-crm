# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_auto_20160426_1417'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='post_text',
            field=models.TextField(max_length=1000, verbose_name='Message'),
        ),
    ]
