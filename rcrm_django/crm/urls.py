from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^auto_complete_inn$', views.auto_complete_inn),
    url(r'^add_task$', views.add_task),
    url(r'^rem_task$', views.rem_task),
    url(r'^task_switch_status$', views.task_switch_status),
    url(r'^hide_closed_tasks$', views.hide_closed_tasks),
    url(r'^only_my_tasks$', views.only_my_tasks),
    url(r'^find_by_inn$', views.find_by_inn),
    url(r'^$', views.hello),
]
