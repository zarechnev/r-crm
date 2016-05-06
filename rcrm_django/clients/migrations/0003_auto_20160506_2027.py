# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0002_auto_20151220_2057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='address',
            field=models.CharField(max_length=300, verbose_name='Organization address'),
        ),
        migrations.AlterField(
            model_name='client',
            name='create_date',
            field=models.DateTimeField(verbose_name='Organization registration date'),
        ),
        migrations.AlterField(
            model_name='client',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='Organization e-mail'),
        ),
        migrations.AlterField(
            model_name='client',
            name='inn',
            field=models.CharField(max_length=15, unique=True, verbose_name='Organization ID'),
        ),
        migrations.AlterField(
            model_name='client',
            name='is_active',
            field=models.BooleanField(verbose_name='Is enabled', default=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='is_deleted',
            field=models.BooleanField(verbose_name='Is deleted', default=False),
        ),
        migrations.AlterField(
            model_name='client',
            name='name',
            field=models.CharField(max_length=200, unique=True, verbose_name='Organization full name'),
        ),
        migrations.AlterField(
            model_name='client',
            name='phone',
            field=models.CharField(max_length=50, verbose_name='Organization phone number'),
        ),
        migrations.AlterField(
            model_name='client',
            name='priority',
            field=models.IntegerField(choices=[('100', 'Наивысший'), ('200', 'Высокий'), ('300', 'Выше среднего'), ('400', 'Средний'), ('500', 'Низкий')], verbose_name='Organization priority'),
        ),
        migrations.AlterField(
            model_name='client',
            name='sname',
            field=models.CharField(max_length=100, unique=True, verbose_name='Organization short name'),
        ),
    ]
