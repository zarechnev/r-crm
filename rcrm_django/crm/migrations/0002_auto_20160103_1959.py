# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='change_status_datetime',
            field=models.DateTimeField(null=True, verbose_name='Дата последнего изменения статуса'),
        ),
        migrations.AlterField(
            model_name='task',
            name='closed_date',
            field=models.DateTimeField(null=True, verbose_name='Дата закрытия заявки'),
        ),
        migrations.AlterField(
            model_name='task',
            name='create_date',
            field=models.DateTimeField(null=True, verbose_name='Дата регистрации заявки'),
        ),
        migrations.AlterField(
            model_name='task',
            name='date_of_removal',
            field=models.DateTimeField(null=True, verbose_name='Дата удаления заявки'),
        ),
    ]
