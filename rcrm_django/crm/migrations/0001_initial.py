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
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('status', models.CharField(max_length=3, choices=[('NEW', 'Новая'), ('PRG', 'Решается'), ('SLD', 'Решена'), ('RMD', 'Удалена')], default='NEW', verbose_name='Статус заявки')),
                ('create_comment', models.CharField(max_length=100, verbose_name='Комментарий')),
                ('is_removed', models.BooleanField(verbose_name='Удалённая заявка', default=False)),
                ('change_status_datetime', models.DateTimeField(verbose_name='Дата последнего изменения статуса', default=0, null=True)),
                ('create_date', models.DateTimeField(verbose_name='Дата регистрации заявки')),
                ('closed_date', models.DateTimeField(verbose_name='Дата закрытия заявки', default=0)),
                ('date_of_removal', models.DateTimeField(verbose_name='Дата удаления заявки', default=0)),
                ('client', models.ForeignKey(verbose_name='Клиент', to='clients.Client')),
                ('create_user', models.ForeignKey(verbose_name='Автор заявки', related_name='create_user', to=settings.AUTH_USER_MODEL)),
                ('remove_user', models.ForeignKey(verbose_name='Удалил заявку', related_name='remove_user', default=0, null=True, to=settings.AUTH_USER_MODEL)),
                ('user_solved', models.ForeignKey(verbose_name='Закрыл заявку', related_name='closed_user', default=0, null=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
