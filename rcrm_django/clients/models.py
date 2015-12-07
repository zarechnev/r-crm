from django.db import models

class Client(models.Model):
    PRIORITY_VALUES = (
        ('100', 'Наивысший'),
        ('200', 'Высокий'),
        ('300', 'Выше среднего'),
        ('400', 'Средний'),
        ('500', 'Низкий'),
    )
    name = models.CharField(max_length=200, unique=True, blank=False, null=False, verbose_name="Полное название организации")
    sname = models.CharField(max_length=100, unique=True, blank=False, null=False, verbose_name="Краткое название организации")
    inn = models.CharField(max_length=15, unique=True, blank=False, null=False, verbose_name="ИНН")
    address = models.CharField(max_length=300, blank=False, null=False, verbose_name="Адрес организации")
    phone = models.CharField(max_length=50, blank=False, null=False, verbose_name="Номер телефона организации")
    email = models.EmailField(unique=True, blank=False, null=False, verbose_name="Электронная почта организации")
    priority = models.IntegerField(choices=PRIORITY_VALUES, verbose_name="Приоритет клиента")
    create_date = models.DateTimeField(verbose_name="Дата регистрации организации")
    is_enabled = models.BooleanField(default=True, verbose_name="Обслуживается")
    is_deleted = models.BooleanField(default=False, verbose_name="Удален")
