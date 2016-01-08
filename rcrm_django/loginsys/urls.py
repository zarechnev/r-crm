from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    url(r'^logout/', 'loginsys.views.logout'),
    url(r'^login/$', 'loginsys.views.login'),
    url(r'^$', 'loginsys.views.login')
    )