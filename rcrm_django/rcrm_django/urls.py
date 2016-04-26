from django.conf.urls import patterns, include, url
from rcrm_django import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'rcrm_django.views.home', name='home'),
    # url(r'^rcrm_django/', include('rcrm_django.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

    url(r'^help/', views.index),
    url(r'^i18n/', include('django.conf.urls.i18n')),

    url(r'^users/', include('users.urls')),
    url(r'^crm/', include('crm.urls')),
    url(r'^clients/', include('clients.urls')),    
    url(r'^statistic/', include('statistic.urls')),
    url(r'^auth/', include('loginsys.urls')),
    url(r'^chat/', include('chat.urls')),
    url(r'^$', include('loginsys.urls')),
)
