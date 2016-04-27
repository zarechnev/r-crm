from django.utils.translation import ugettext_lazy as _
from django.db import models

class Client(models.Model):
    #TODO: Реализовать методы и свойства по аналогии с разделом задач
    PRIORITY_VALUES = (
        ('100', 'Наивысший'),
        ('200', 'Высокий'),
        ('300', 'Выше среднего'),
        ('400', 'Средний'),
        ('500', 'Низкий'),
    )
    name = models.CharField(max_length=200, unique=True, blank=False, null=False,
                            verbose_name=_("Organization full name"))
    sname = models.CharField(max_length=100, unique=True, blank=False, null=False,
                             verbose_name=_("Organization short name"))
    inn = models.CharField(max_length=15, unique=True, blank=False, null=False, verbose_name=_("Organization ID"))
    address = models.CharField(max_length=300, blank=False, null=False, verbose_name=_("Organization address"))
    phone = models.CharField(max_length=50, blank=False, null=False, verbose_name=_("Organization phone number"))
    email = models.EmailField(unique=True, blank=False, null=False, verbose_name=_("Organization e-mail"))
    priority = models.IntegerField(choices=PRIORITY_VALUES, verbose_name=_("Organization priority"))
    create_date = models.DateTimeField(verbose_name=_("Organization registration date"))
    is_active = models.BooleanField(default=True, blank=False, verbose_name=_("Is enabled"))
    is_deleted = models.BooleanField(default=False, verbose_name=_("Is deleted"))
