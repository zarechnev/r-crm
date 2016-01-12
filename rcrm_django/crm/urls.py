from django.conf.urls import patterns, url


urlpatterns = patterns('',
    url(r'^auto_complite_inn$', 'crm.views.auto_complite_inn'),
    url(r'^add_task$', 'crm.views.add_task'),
    url(r'^rem_task$', 'crm.views.rem_task'),
    url(r'^task_switch_status$', 'crm.views.task_switch_status'),
    url(r'^closed_invisible$', 'crm.views.closed_invisible'),
    url(r'^$', 'crm.views.hello')
)