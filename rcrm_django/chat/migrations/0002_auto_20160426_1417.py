# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='create_post_user',
            field=models.ForeignKey(related_name='create_post_user', verbose_name='Author', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='chat',
            name='post_date',
            field=models.DateTimeField(verbose_name='Message date'),
        ),
        migrations.AlterField(
            model_name='chat',
            name='post_text',
            field=models.TextField(max_length=1000, verbose_name='Massage'),
        ),
    ]
