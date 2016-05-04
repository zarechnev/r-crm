from django.utils.translation import ugettext_lazy as _
from django.db import models
from clients.models import Client
from django.contrib import auth


class Priority(models.Model):
    priority_ru = models.CharField(max_length=50)
    priority_en = models.CharField(max_length=50)
    weight = models.IntegerField(verbose_name=_("Weight"), default=25)
    default = models.BooleanField()


class Task(models.Model):
    STATUS_TO_TEMLATE = {
        'NEW': 'Новая',
        'PRG': 'Решается',
        'SLD': 'Решена'
    }
    STATUS_OF_TASK = STATUS_TO_TEMLATE.keys()

    status = models.CharField(blank=False, null=False, max_length=3, verbose_name=_("Task status"))
    task_prio = models.ForeignKey(Priority, blank=False, null=False, verbose_name=_("Task priority"))
    create_comment = models.CharField(blank=False, null=False, max_length=200, verbose_name=_("Comment"))
    is_removed = models.BooleanField(default=False, blank=False, verbose_name=_("Deleted task"))
    change_status_datetime = models.DateTimeField(null=True, blank=False,
                                                  verbose_name=_("Last modify date"))

    create_user = models.ForeignKey(auth.models.User, null=False, blank=False, related_name='create_user',
                                    verbose_name=_("Task author"))
    solves_user = models.ForeignKey(auth.models.User, null=True, blank=False, default=0, related_name='solves_user',
                                    verbose_name=_("Solves user"))
    user_solved = models.ForeignKey(auth.models.User, null=True, blank=False, default=0, related_name='user_solved',
                                    verbose_name=_("Solved user"))
    remove_user = models.ForeignKey(auth.models.User, null=True, blank=False, default=0, related_name='remove_user',
                                    verbose_name=_("Who was remove the task"))

    client = models.ForeignKey(Client, null=False, blank=False, verbose_name=_("Client"))

    create_date = models.DateTimeField(null=True, blank=False, verbose_name=_("Create task date"))
    closed_date = models.DateTimeField(null=True, blank=False, verbose_name=_("Close task date"))
    date_of_removal = models.DateTimeField(null=True, blank=False, verbose_name=_("Remove task date"))

    def set_status(self, stat):
        if stat in self.STATUS_OF_TASK:
            self.status = stat
        else:
            return "Bad status!"

    def status_to_template(self):
        if self.status in self.STATUS_TO_TEMLATE:
            return self.STATUS_TO_TEMLATE[self.status]
        else:
            return "Bad status!"
