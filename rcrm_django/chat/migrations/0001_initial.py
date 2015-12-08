# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('post_text', models.TextField(max_length=1000, verbose_name='Текст')),
                ('post_date', models.DateTimeField(verbose_name='Дата сообщения')),
                ('create_post_user', models.ForeignKey(related_name='create_post_user', to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
            ],
        ),
    ]
