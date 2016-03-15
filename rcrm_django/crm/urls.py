from django.conf.urls import patterns, url


urlpatterns = patterns('',
    url(r'^auto_complite_inn$', 'crm.views.auto_complite_inn'),
    url(r'^add_task$', 'crm.views.add_task'),
    url(r'^rem_task$', 'crm.views.rem_task'),
    url(r'^task_switch_status$', 'crm.views.task_switch_status'),
    url(r'^hide_closed_tasks$', 'crm.views.hide_closed_tasks'),
    url(r'^only_my_tasks$', 'crm.views.only_my_tasks'),
    url(r'^find_by_inn$', 'crm.views.find_by_inn'),
    url(r'^$', 'crm.views.hello')
)