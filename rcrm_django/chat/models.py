from django.db import models
from django.contrib import auth
from clients.models import Client


class Chat(models.Model):
    create_post_user = models.ForeignKey(auth.models.User, related_name='create_post_user', verbose_name="Автор")
    post_text = models.TextField(max_length=1000, verbose_name="Текст")
    post_date = models.DateTimeField(verbose_name="Дата сообщения")
