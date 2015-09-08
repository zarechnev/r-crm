from django.conf.urls import patterns, url


urlpatterns = patterns('',
    url(r'^auto_complite_inn$', 'crm.views.auto_complite_inn'),
    url(r'^add_task$', 'crm.views.add_task'),
    url(r'^rem_task$', 'crm.views.rem_task'),
    url(r'^$', 'crm.views.hello')
)


