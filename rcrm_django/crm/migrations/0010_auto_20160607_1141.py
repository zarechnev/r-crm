# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0009_auto_20160506_2027'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubTask',
            fields=[
                ('task_ptr', models.OneToOneField(serialize=False, auto_created=True, to='crm.Task', primary_key=True, parent_link=True)),
            ],
            bases=('crm.task',),
        ),
        migrations.AlterField(
            model_name='task',
            name='closed_date',
            field=models.DateTimeField(verbose_name='Close date', null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='pick_date',
            field=models.DateTimeField(verbose_name='Date of receipt', null=True),
        ),
        migrations.AddField(
            model_name='subtask',
            name='parent',
            field=models.ForeignKey(to='crm.Task', verbose_name='Parent task', related_name='parent_task'),
        ),
    ]
