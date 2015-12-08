# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(verbose_name='Полное название организации', unique=True, max_length=200)),
                ('sname', models.CharField(verbose_name='Краткое название организации', unique=True, max_length=100)),
                ('inn', models.CharField(verbose_name='ИНН', unique=True, max_length=15)),
                ('address', models.CharField(verbose_name='Адрес организации', max_length=300)),
                ('phone', models.CharField(verbose_name='Номер телефона организации', max_length=50)),
                ('email', models.EmailField(verbose_name='Электронная почта организации', unique=True, max_length=254)),
                ('priority', models.IntegerField(verbose_name='Приоритет клиента', choices=[('100', 'Наивысший'), ('200', 'Высокий'), ('300', 'Выше среднего'), ('400', 'Средний'), ('500', 'Низкий')])),
                ('create_date', models.DateTimeField(verbose_name='Дата регистрации организации')),
                ('is_enabled', models.BooleanField(verbose_name='Обслуживается', default=True)),
                ('is_deleted', models.BooleanField(verbose_name='Удален', default=False)),
            ],
        ),
    ]
