# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('crm', '0002_auto_20160103_1959'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='solves_user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='Решает заявку', default=0, related_name='solves_user', null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('NEW', 'Новая'), ('PRG', 'Решается'), ('SLD', 'Решена'), ('RMD', 'Удалена')], verbose_name='Статус заявки', max_length=3),
        ),
        migrations.AlterField(
            model_name='task',
            name='user_solved',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='Закрыл заявку', default=0, related_name='user_solved', null=True),
        ),
    ]
