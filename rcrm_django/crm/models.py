from django.db import models
from clients.models import Client
from django.contrib import auth


class Task(models.Model):
    STATUS_OF_TASK = (
        ('NEW', 'Новая'),
        ('PRG', 'Решается'),
        ('SLD', 'Решена'),
        ('RMD', 'Удалена'),
    )

    status = models.CharField( blank=False, null=False, max_length=3, choices=STATUS_OF_TASK, default='NEW', verbose_name="Статус заявки" )
    create_comment = models.CharField( blank=False, null=False, max_length=100, verbose_name="Комментарий" )
    is_removed = models.BooleanField( default=False, blank=False, verbose_name="Удалённая заявка" )
    change_status_datetime = models.DateTimeField( null=True, blank=False, verbose_name="Дата последнего изменения статуса" )

    create_user = models.ForeignKey( auth.models.User, null=False, blank=False, related_name='create_user', verbose_name="Автор заявки" )
    user_solved = models.ForeignKey( auth.models.User, null=True, blank=False, default=0, related_name='closed_user', verbose_name="Закрыл заявку" )
    remove_user = models.ForeignKey( auth.models.User, null=True, blank=False, default=0, related_name='remove_user', verbose_name="Удалил заявку" )

    client = models.ForeignKey( Client, null=False, blank=False, verbose_name="Клиент" )

    create_date = models.DateTimeField( null=True, blank=False, verbose_name="Дата регистрации заявки" )
    closed_date = models.DateTimeField( null=True, blank=False, verbose_name="Дата закрытия заявки" )
    date_of_removal = models.DateTimeField( null=True, blank=False, verbose_name="Дата удаления заявки" )
