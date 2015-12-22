# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('clients', '0002_auto_20151220_2057'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('status', models.CharField(max_length=100, default='new', verbose_name='Статус заявки')),
                ('create_date', models.DateTimeField(verbose_name='Дата регистрации заявки')),
                ('closed_date', models.DateTimeField(null=True, blank=True, verbose_name='Дата закрытия заявки')),
                ('create_comment', models.CharField(null=True, max_length=100, blank=True, verbose_name='Комментарий')),
                ('is_removed', models.BooleanField(default=False, verbose_name='Удалённая заявка')),
                ('date_of_removal', models.DateTimeField(null=True, blank=True, verbose_name='Дата удаления заявки')),
                ('client', models.ForeignKey(to='clients.Client', verbose_name='Организция/Клиент')),
                ('closed_user', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True, blank=True, related_name='closed_user', verbose_name='Закрыл заявку')),
                ('create_user', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='create_user', verbose_name='Автор заявки')),
                ('remove_user', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True, blank=True, related_name='remove_user', verbose_name='Удалил заявку')),
            ],
        ),
    ]
