# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0005_task_task_prio'),
    ]

    operations = [
        migrations.CreateModel(
            name='Priority',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('priority_ru', models.CharField(max_length=50)),
                ('priority_en', models.CharField(max_length=50)),
                ('default', models.BooleanField()),
            ],
        ),
        migrations.AlterField(
            model_name='task',
            name='task_prio',
            field=models.ForeignKey(verbose_name='Приоритет заявки', to='crm.Priority'),
        ),
    ]
