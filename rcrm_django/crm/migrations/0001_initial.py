# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('create_date', models.DateTimeField(verbose_name='Дата регистрации заявки')),
                ('closed_date', models.DateTimeField(verbose_name='Дата закрытия заявки', blank=True, null=True)),
                ('create_comment', models.CharField(verbose_name='Комментарий', blank=True, max_length=100, null=True)),
                ('is_removed', models.BooleanField(verbose_name='Удалённая заявка', default=False)),
                ('date_of_removal', models.DateTimeField(verbose_name='Дата удаления заявки', blank=True, null=True)),
                ('client', models.ForeignKey(to='clients.Client', verbose_name='Организция/Клиент')),
                ('closed_user', models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='Закрыл заявку', blank=True, related_name='closed_user', null=True)),
                ('create_user', models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='Автор заявки', related_name='create_user')),
                ('remove_user', models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='Удалил заявку', blank=True, related_name='remove_user', null=True)),
            ],
        ),
    ]
