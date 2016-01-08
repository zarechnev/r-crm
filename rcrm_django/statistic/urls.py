from django.conf.urls import patterns, url


urlpatterns = patterns('',
    url(r'^$', 'statistic.views.hello'),
    url(r'^users$', 'statistic.views.users'),
    url(r'^clients$', 'statistic.views.clients'),
    url(r'^tasks$', 'statistic.views.tasks')
)
