from django.db import models
from clients.models import Client
from django.contrib import auth


class Task(models.Model):
    create_user = models.ForeignKey(auth.models.User, related_name='create_user', verbose_name="Автор заявки")
    closed_user = models.ForeignKey(auth.models.User, null=True, blank=True, related_name='closed_user', verbose_name="Закрыл заявку")
    remove_user = models.ForeignKey(auth.models.User, null=True, blank=True, related_name='remove_user', verbose_name="Удалил заявку")
    status = models.CharField(blank=False, null=False, max_length=100, default="new", verbose_name="Статус заявки")
    client = models.ForeignKey(Client, verbose_name="Организция/Клиент")
    create_date = models.DateTimeField(verbose_name="Дата регистрации заявки")
    closed_date = models.DateTimeField(blank=True, null=True, verbose_name="Дата закрытия заявки")
    create_comment = models.CharField(blank=True, null=True, max_length=100, verbose_name="Комментарий")
    is_removed = models.BooleanField(default=False, verbose_name="Удалённая заявка")
    date_of_removal = models.DateTimeField(blank=True, null=True, verbose_name="Дата удаления заявки")