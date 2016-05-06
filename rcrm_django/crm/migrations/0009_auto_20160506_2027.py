# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0008_priority_weight'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='pick_date',
            field=models.DateTimeField(null=True, verbose_name='Pic by engineer date'),
        ),
        migrations.AlterField(
            model_name='priority',
            name='weight',
            field=models.IntegerField(verbose_name='Weight', default=25),
        ),
        migrations.AlterField(
            model_name='task',
            name='change_status_datetime',
            field=models.DateTimeField(null=True, verbose_name='Last modify date'),
        ),
        migrations.AlterField(
            model_name='task',
            name='client',
            field=models.ForeignKey(to='clients.Client', verbose_name='Client'),
        ),
        migrations.AlterField(
            model_name='task',
            name='closed_date',
            field=models.DateTimeField(null=True, verbose_name='Close task date'),
        ),
        migrations.AlterField(
            model_name='task',
            name='create_comment',
            field=models.CharField(max_length=200, verbose_name='Comment'),
        ),
        migrations.AlterField(
            model_name='task',
            name='create_date',
            field=models.DateTimeField(null=True, verbose_name='Create task date'),
        ),
        migrations.AlterField(
            model_name='task',
            name='create_user',
            field=models.ForeignKey(verbose_name='Task author', to=settings.AUTH_USER_MODEL, related_name='create_user'),
        ),
        migrations.AlterField(
            model_name='task',
            name='date_of_removal',
            field=models.DateTimeField(null=True, verbose_name='Remove task date'),
        ),
        migrations.AlterField(
            model_name='task',
            name='is_removed',
            field=models.BooleanField(verbose_name='Deleted task', default=False),
        ),
        migrations.AlterField(
            model_name='task',
            name='remove_user',
            field=models.ForeignKey(null=True, verbose_name='Who was remove the task', default=0, to=settings.AUTH_USER_MODEL, related_name='remove_user'),
        ),
        migrations.AlterField(
            model_name='task',
            name='solves_user',
            field=models.ForeignKey(null=True, verbose_name='Solves user', default=0, to=settings.AUTH_USER_MODEL, related_name='solves_user'),
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(max_length=3, verbose_name='Task status'),
        ),
        migrations.AlterField(
            model_name='task',
            name='task_prio',
            field=models.ForeignKey(to='crm.Priority', verbose_name='Task priority'),
        ),
        migrations.AlterField(
            model_name='task',
            name='user_solved',
            field=models.ForeignKey(null=True, verbose_name='Solved user', default=0, to=settings.AUTH_USER_MODEL, related_name='user_solved'),
        ),
    ]
